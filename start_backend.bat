@echo off
echo Starting ShopSmart RAG Backend (FastAPI)...
cd /d "%~dp0"
uv run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
