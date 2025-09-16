# Claude Code Project Instructions

## Project Overview
This is a FastAPI-based time service that provides a simple GET /time endpoint returning the server's local time.

## Development Commands
- **Start server**: `python3 main.py` or `uvicorn main:app --reload`
- **Run tests**: `pytest tests/`
- **Install dependencies**: `pip install -r requirements.txt`

## Project Structure
- `main.py` - FastAPI application with /time endpoint
- `tests/test_main.py` - Unit tests
- `requirements.txt` - Python dependencies

## API Documentation
Available at `http://localhost:8000/docs` when server is running.