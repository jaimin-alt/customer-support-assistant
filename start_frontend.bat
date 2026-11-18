@echo off
echo Starting ShopSmart RAG Frontend (Streamlit)...
cd /d "%~dp0"
uv run streamlit run frontend/app.py --server.port 8501
