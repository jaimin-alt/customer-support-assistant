"""
Streamlit frontend for the ShopSmart RAG chatbot.

Run with:
    streamlit run frontend/app.py
"""

import json
import requests
import streamlit as st

# ── Configuration ──────────────────────────────────────────────────────────
API_BASE = "http://localhost:8000"
STREAM_URL = f"{API_BASE}/chat/stream"
HEALTH_URL = f"{API_BASE}/health"

# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ShopSmart Support",
    page_icon="🛒",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* Source badge styling */
    .source-badge {
        display: inline-block;
        background: #1e3a5f;
        color: #e8f4fd;
        border-radius: 6px;
        padding: 3px 10px;
        margin: 3px 4px;
        font-size: 0.82rem;
        font-weight: 500;
        border: 1px solid #2d5a8e;
    }
    .source-badge span.pdf-icon {
        margin-right: 5px;
    }
    .sources-container {
        margin-top: 10px;
        padding: 10px 14px;
        background: #0f2235;
        border-left: 3px solid #4a9ede;
        border-radius: 4px;
    }
    .sources-title {
        font-size: 0.8rem;
        color: #8bb8d8;
        font-weight: 600;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Header ─────────────────────────────────────────────────────────────────
st.title("🛒 ShopSmart Customer Support")
st.caption("Powered by RAG — answers grounded in our official policy documents.")

# ── Sidebar: status & settings ─────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    top_k = st.slider(
        "Chunks to retrieve (top_k)",
        min_value=1, max_value=10, value=4,
        help="How many document chunks the retriever fetches before the LLM answers.",
    )

    st.divider()
    st.subheader("🔌 Backend Status")
    if st.button("Check connection", use_container_width=True):
        try:
            resp = requests.get(HEALTH_URL, timeout=10)
            if resp.status_code == 200:
                info = resp.json()
                st.success("✅ Connected")
                st.metric("Collection", info.get("collection", "—"))
                st.metric("Chunks indexed", info.get("chunks_stored", "—"))
            else:
                st.error(f"❌ Backend returned {resp.status_code}")
        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. The backend server may still be initializing or busy.")
        except requests.exceptions.ConnectionError:
            st.error(
                "❌ Cannot reach backend.\n\n"
                "Make sure FastAPI is running on port 8000:\n"
                "```\nuv run uvicorn backend.main:app --reload --port 8000\n```"
            )
        except Exception as err:
            st.error(f"❌ Connection error: {err}")

    st.divider()
    if st.button("🗑️ Clear chat history", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ── Chat state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []


def render_sources_html(sources: list[dict]) -> str:
    """Render a nicely formatted source badges block."""
    if not sources:
        return ""
    badges = ""
    for s in sources:
        pdf_name = s.get("source", "unknown")
        page = s.get("page_number", "?")
        # Show only the filename, not the full path
        import os
        pdf_name = os.path.basename(pdf_name)
        badges += (
            f'<span class="source-badge">'
            f'<span class="pdf-icon">📄</span>{pdf_name} · p.{page}'
            f'</span>'
        )
    return (
        f'<div class="sources-container">'
        f'<div class="sources-title">📚 Sources</div>'
        f'{badges}'
        f'</div>'
    )


# ── Render existing chat history ───────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            st.markdown(render_sources_html(msg["sources"]), unsafe_allow_html=True)


# ── Chat input ─────────────────────────────────────────────────────────────
if prompt := st.chat_input("Ask a question about ShopSmart policies…"):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream assistant response
    with st.chat_message("assistant"):
        answer_placeholder = st.empty()
        sources_placeholder = st.empty()

        full_answer = ""
        sources = []
        had_error = False

        try:
            with requests.post(
                STREAM_URL,
                json={"question": prompt, "top_k": top_k},
                stream=True,
                timeout=120,
            ) as response:
                if response.status_code != 200:
                    st.error(f"Backend error: {response.status_code} — {response.text}")
                    had_error = True
                else:
                    # Parse SSE events line by line
                    event_type = None
                    for line in response.iter_lines(decode_unicode=True):
                        if not line:
                            # Blank line = end of event block
                            event_type = None
                            continue

                        if line.startswith("event:"):
                            event_type = line[len("event:"):].strip()

                        elif line.startswith("data:"):
                            raw = line[len("data:"):].strip()
                            if not raw or raw == "{}":
                                continue
                            try:
                                payload = json.loads(raw)
                            except json.JSONDecodeError:
                                continue

                            if event_type == "token":
                                full_answer += payload.get("token", "")
                                answer_placeholder.markdown(full_answer + "▌")

                            elif event_type == "sources":
                                sources = payload.get("sources", [])
                                if sources:
                                    sources_placeholder.markdown(
                                        render_sources_html(sources),
                                        unsafe_allow_html=True,
                                    )

                            elif event_type == "error":
                                st.error(f"⚠️ {payload.get('error', 'Unknown error')}")
                                had_error = True

                            elif event_type == "done":
                                break

        except requests.exceptions.ConnectionError:
            st.error(
                "❌ Cannot connect to the backend.\n\n"
                "Start it with:\n```\nuv run uvicorn backend.main:app --reload\n```"
            )
            had_error = True
        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. The backend may be overloaded.")
            had_error = True

        # Final render (remove cursor)
        if full_answer:
            answer_placeholder.markdown(full_answer)
        elif not had_error:
            answer_placeholder.markdown(
                "_No answer was generated. The question may be outside the knowledge base._"
            )

        # Show sources below final answer
        if sources:
            sources_placeholder.markdown(
                render_sources_html(sources), unsafe_allow_html=True
            )
        elif not had_error and not sources:
            sources_placeholder.markdown(
                "_⚠️ No relevant policy documents found for this question._"
            )

    # Persist to session state
    if not had_error:
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_answer,
            "sources": sources,
        })
