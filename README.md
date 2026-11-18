# 🛒 ShopSmart RAG — Customer Support Chatbot

An end-to-end, production-grade **Retrieval-Augmented Generation (RAG)** customer support chatbot. It answers customer queries strictly grounded in official policy PDF documents, streams responses in real time, and attributes every answer to its exact source document and page number.

Built with a decoupled **FastAPI** backend and an interactive **Streamlit** frontend.

---

## 📌 Table of Contents
1. [Overview & Architecture](#-overview--architecture)
2. [End-to-End Request Lifecycle](#-end-to-end-request-lifecycle)
3. [Tech Stack](#-tech-stack)
4. [Project Structure](#-project-structure)
5. [Chat History & Context Behavior](#-chat-history--context-behavior)
6. [Prerequisites & Installation](#-prerequisites--installation)
7. [How to Run](#-how-to-run)
8. [Offline Vector Indexing](#-offline-vector-indexing)
9. [Configuration](#-configuration)
10. [Testing & Verification](#-testing--verification)
11. [Troubleshooting](#-troubleshooting)

---

## 🚀 Overview & Architecture

Standard LLMs suffer from hallucinations and lack domain-specific policies. This project implements a grounded RAG architecture that limits the model's domain knowledge to ShopSmart's official PDF manuals and policy agreements.

```
┌─────────────────────────────────────────────────────────────┐
│                      STREAMLIT FRONTEND                     │
│  - User Question Input                                      │
│  - Real-time Token Streaming via Server-Sent Events (SSE)   │
│  - Source Attribution Badges (PDF Filename + Page Number)   │
│  - Session History (st.session_state)                       │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP POST /chat/stream
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                       FASTAPI BACKEND                       │
│  - Endpoint: /chat/stream (StreamingResponse)               │
│  - Endpoint: /health (Instant status check)                 │
│  - Background embedding model pre-warming (Lifespan)        │
└──────────────┬───────────────────────────────┬──────────────┘
               │                               │
       1. Query Embedding                      │ 3. Context Grounded
       & Semantic Retrieval                    │    Prompt + Stream
               ▼                               ▼
┌──────────────────────────────┐ ┌────────────────────────────┐
│      CHROMADB VECTOR DB      │ │          GROQ LLM          │
│ - sentence-transformers /    │ │ - Model: openai/gpt-oss-20b│
│   all-MiniLM-L6-v2           │ │   (or configured model)    │
│ - 186 Chunks Indexed         │ │ - Zero Temperature (T=0)   │
│ - Normalized L2 Similarity   │ │ - Streaming Generation     │
└──────────────────────────────┘ └────────────────────────────┘
```

---

## 🔄 End-to-End Request Lifecycle

Here is what happens step-by-step from the moment a user types a question to the rendered answer:

```
User types query
       │
       ▼
1. Frontend [Streamlit]:
   Captures input and sends an HTTP POST request to http://localhost:8000/chat/stream
   Payload: { "question": "What is the return policy?", "top_k": 4 }
       │
       ▼
2. Backend [FastAPI]:
   Validates request payload with Pydantic.
       │
       ▼
3. Semantic Retrieval [ChromaDB + sentence-transformers]:
   - Converts user question into a dense 384-dimensional vector using `all-MiniLM-L6-v2`.
   - ChromaDB searches the 186 pre-indexed policy chunks and returns top-k nearest neighbors.
   - Chunks are converted into relevance scores and deduplicated by `(source, page_number)`.
       │
       ▼
4. Immediate Source Emission [SSE]:
   FastAPI immediately yields an SSE event:
   event: sources
   data: {"sources": [{"source": "return_refund_policy.pdf", "page_number": 2}, ...]}
   Streamlit receives this and instantly displays the PDF citation badges.
       │
       ▼
5. Prompt Construction [LangChain]:
   Retrieved chunks are structured into context strings:
   System: "You are a customer-support assistant for ShopSmart... Answer ONLY from context..."
   Context: [Source 1: return_refund_policy.pdf, page 2] ...
   Human: "What is the return policy?"
       │
       ▼
6. Stream Generation [Groq Cloud API]:
   - Calls Groq's high-speed inference engine (`openai/gpt-oss-20b` or LLaMA models).
   - Generates tokens at ~200+ tokens/sec.
       │
       ▼
7. Token Streaming [SSE -> Streamlit]:
   FastAPI yields each token:
   event: token
   data: {"token": "ShopSmart "}
   Streamlit consumes lines via `iter_lines()`, appends them to placeholder `full_answer + "▌"`.
       │
       ▼
8. Stream Completion:
   FastAPI emits `event: done`. Streamlit finalizes markdown text, removes cursor `▌`,
   and stores the message and citations in session state.
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Streamlit (`>=1.67.0`) | Interactive web UI, real-time SSE stream consumption, session management |
| **Backend API** | FastAPI (`>=0.164.0`) + Uvicorn | High-performance asynchronous API server with Server-Sent Events (SSE) |
| **Vector Database** | ChromaDB (`langchain-chroma >=1.1.0`) | Local, persistent vector store (stores 186 chunk embeddings + metadata) |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` | Dense 384-dim semantic embeddings running locally on CPU |
| **LLM Inference** | Groq Cloud (`langchain-groq >=1.1.3`) | Ultra-fast token generation (`openai/gpt-oss-20b` or LLaMA-3.3) |
| **Orchestration** | LangChain Core & Community | Document loaders, chunking strategies, prompt templates, stream bindings |
| **PDF Extraction** | PyPDF (`>=6.21.4`) | Text extraction, page normalization, and metadata tagging |
| **Package Manager** | `uv` (Astral) | Extremely fast Python package management and virtual environment tool |

---

## 📂 Project Structure

```
RAG/
├── backend/
│   ├── __init__.py
│   └── main.py              # FastAPI server (SSE streaming endpoint + health check)
├── frontend/
│   └── app.py               # Streamlit chat interface with streaming and badges
├── knowledge-base/
│   ├── pdf/                 # 8 ShopSmart official policy documents (source of truth)
│   └── md/                  # Markdown mirrors (for easy reference & audits)
├── chroma_db/               # Persisted vector database (186 indexed chunks)
├── src/rag/
│   ├── __init__.py
│   ├── config.py            # Centralized settings & environment loader
│   ├── document_loader.py   # PDF discovery, loading & metadata extraction
│   ├── text_splitter.py     # Deterministic chunking & unique chunk IDs
│   ├── embeddings.py        # Sentence-transformers singleton & caching
│   ├── vector_store.py      # ChromaDB initialization, upsert & collection info
│   ├── retriever.py         # Semantic search, score normalization & filtering
│   ├── prompts.py           # Guardrailed system & user prompt templates
│   └── rag_chain.py         # End-to-end retrieval, prompt binding & streaming
├── tests/
│   └── test_rag_pipeline.py # Unit & integration test suite
├── indexing.py              # CLI script to parse PDFs and populate ChromaDB
├── rag_chat.py              # CLI interactive terminal chatbot
├── run_tests.py             # Standalone test runner (no pytest required)
├── start_backend.bat        # Windows one-click script to launch FastAPI
├── start_frontend.bat       # Windows one-click script to launch Streamlit
├── pyproject.toml           # Project dependencies & package metadata
└── .env                     # Secrets & API credentials (not committed)
```

---

## 💬 Chat History & Context Behavior

### 1. How is Chat History Saved?
* **Storage Location:** Chat history is stored in the **browser session memory** via Streamlit's `st.session_state.messages`.
* **Structure:**
  ```python
  st.session_state.messages = [
      {"role": "user", "content": "What is the return window?"},
      {
          "role": "assistant",
          "content": "ShopSmart offers a 30-day return window...",
          "sources": [{"source": "return_refund_policy.pdf", "page_number": 2}]
      }
  ]
  ```
* **Lifespan:** The history persists as long as the browser tab remains open. A "Clear chat history" button in the sidebar resets `st.session_state.messages = []`.

### 2. Does the LLM Currently Have Access to Chat History?
* **Current Behavior:** **No.** Each question submitted by the user is processed as an **independent single-turn query**.
* When the user submits a message, the frontend sends only the current string `{ "question": prompt, "top_k": top_k }` to `/chat/stream`.
* ChromaDB searches documents relevant to *that exact sentence*, and the prompt sent to Groq contains only the retrieved PDF context and the single question.

### 3. How to Enable Multi-Turn Conversational Memory (Future Extension)
To make the chatbot answer follow-up questions (e.g. *"What did you say about electronics in the previous answer?"*):
1. **Pass History:** Update `ChatRequest` in `backend/main.py` to accept `history: list[dict]`.
2. **Query Reformulation:** Before calling ChromaDB, use a lightweight LLM call to condense chat history + new question into a standalone question:
   * *User:* "What about laptops?" -> *Rewritten Query:* "What is the return policy for laptop computers?"
3. **Include History in Prompt:** Pass `AIMessage` and `HumanMessage` history into `llm.stream([system_msg, *history, human_msg])`.

---

## ⚙️ Prerequisites & Installation

### 1. Prerequisites
* **Python**: Version `3.11` or higher installed.
* **uv**: Recommended Python package manager ([install instructions](https://github.com/astral-sh/uv)):
  ```powershell
  # Windows (PowerShell)
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
* **Groq API Key**: A free API key from [Groq Console](https://console.groq.com/).

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/customer-support-agent.git
cd customer-support-agent/RAG
```

### 3. Install Dependencies
Using `uv`, all dependencies and virtual environments are installed automatically with a single command:
```bash
uv sync
```

### 4. Configure Environment Variables
Create a `.env` file in the `RAG/` root folder:
```env
GROQ_API_KEY=gsk_your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```
*(You can also use any other supported Groq model like `llama-3.3-70b-versatile` or `llama-3.1-8b-instant`).*

---

## 🏃 How to Run

### Option A: Using Windows Batch Files (Easiest)
1. Double-click `start_backend.bat` (Starts FastAPI on `http://localhost:8000`).
2. Double-click `start_frontend.bat` (Starts Streamlit on `http://localhost:8501`).

---

### Option B: Using Terminal Commands

#### Step 1 — Start FastAPI Backend:
In Terminal 1:
```bash
uv run uvicorn backend.main:app --reload --port 8000
```
Wait until you see:
```text
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

#### Step 2 — Start Streamlit Frontend:
In Terminal 2:
```bash
uv run streamlit run frontend/app.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser.

---

### Option C: Terminal CLI Chat (No Browser Needed)
To test the pipeline directly in your console:
```bash
# Interactive chat
uv run python rag_chat.py

# Debug mode (displays retrieved chunks, distance scores & excerpts)
uv run python rag_chat.py --debug
```

---

## 🗄️ Offline Vector Indexing

The repository comes with a pre-indexed vector store in `chroma_db/` (186 chunks). However, if you add new PDF files to `knowledge-base/pdf/` or edit existing policies, run the indexer:

```bash
# Incremental update (uses deterministic chunk IDs; skips unchanged chunks)
uv run python indexing.py

# Full clean rebuild (deletes old ChromaDB collection and re-indexes from scratch)
uv run python indexing.py --rebuild
```

**Indexing Steps:**
1. **PDF Discovery:** Scans `knowledge-base/pdf/*.pdf`.
2. **Text Extraction:** Normalizes whitespace and extracts page-level metadata.
3. **Recursive Chunking:** Splits pages into 1,000-character segments with 150-character overlap.
4. **Deterministic Hashing:** Generates chunk IDs based on `hash(source_filename + page_num + chunk_index)`.
5. **Local Vectorization:** Embeds chunks via `sentence-transformers/all-MiniLM-L6-v2`.
6. **Upsert:** Inserts vectors and metadata into `./chroma_db`.

---

## 🔧 Configuration Reference

All tunable parameters are centrally managed in `src/rag/config.py`:

| Variable | Default Value | Description |
|---|---|---|
| `GROQ_API_KEY` | *(from .env)* | Groq API authentication token |
| `GROQ_MODEL` | *(from .env)* | Groq chat model identifier |
| `EMBEDDING_MODEL_NAME` | `sentence-transformers/all-MiniLM-L6-v2` | HuggingFace embedding model |
| `CHROMA_COLLECTION_NAME`| `shopsmart_knowledge` | ChromaDB collection identifier |
| `DEFAULT_CHUNK_SIZE` | `1000` | Target character size per text chunk |
| `DEFAULT_CHUNK_OVERLAP` | `150` | Overlap between adjacent chunks |
| `DEFAULT_TOP_K` | `4` | Number of chunks fetched per user query |
| `LLM_TEMPERATURE` | `0` | Generation temperature (0 ensures factual consistency) |

---

## 🧪 Testing & Verification

Run the test suite to verify pipeline integrity:

```bash
# Run standalone test runner (no pytest required)
uv run python run_tests.py

# Run with pytest (unit + integration tests)
uv run python -m pytest tests/ -v

# Run without live LLM calls (tests offline retrieval & chunking only)
uv run python -m pytest tests/ -v -m "not live"
```

---

## ❓ Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| `ReadTimeoutError: HTTPConnectionPool... timeout=5` | Backend took longer to load PyTorch during initial cold-start. | The latest update fixes this with background pre-warming. Ensure FastAPI is fully running before clicking "Check connection". |
| `Cannot reach backend` in Streamlit | FastAPI server is not running on port 8000. | Run `uv run uvicorn backend.main:app --reload --port 8000` in a separate terminal. |
| `GROQ_API_KEY is not set` | Missing `.env` file or variable. | Create `.env` in `RAG/` root and add `GROQ_API_KEY=gsk_...`. |
| `Vector store is empty` | `chroma_db/` folder missing or empty. | Run `uv run python indexing.py` to index the PDFs. |
| `UnicodeEncodeError` on Windows | Default Windows PowerShell encoding mismatch. | Handled automatically by `backend/main.py` and `rag_chat.py`. |

---

## 📄 License & Attribution
Designed and built for ShopSmart E-Commerce Support System. Developed with LangChain, FastAPI, Streamlit, and Groq.
