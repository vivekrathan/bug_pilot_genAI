
# GenAI-Based Intelligent Bug Triage and Root Cause Analysis Assistant

A Retrieval-Augmented Generation (RAG) application that helps
developers analyze software bug reports using Google's Gemini LLM.

## Features

- Bug report analysis using Gemini
- Semantic retrieval using Sentence Transformers
- Vector storage using ChromaDB
- Similar historical issue retrieval
- Root-cause hypotheses
- Severity classification with explanations
- Debugging steps and suggested fixes
- Add knowledge documents through the API

## Architecture

Bug Report
    -> FastAPI
    -> Sentence Transformer Embeddings
    -> ChromaDB Retrieval
    -> Gemini LLM
    -> Structured Triage Report

## Setup

1. Create a virtual environment.

   python -m venv .venv

2. Activate it on Windows PowerShell.

   .\.venv\Scripts\Activate.ps1

3. Install dependencies.

   pip install -r requirements.txt

4. Create a .env file and add your Gemini API key.

   GEMINI_API_KEY=your_key
   GEMINI_MODEL=gemini-3.8-flash

5. Start the application.

   python -m uvicorn app.main:app --reload

6. Open the API documentation.

   http://127.0.0.1:8000/docs

## API Endpoints

GET /

GET /health

POST /triage

POST /knowledge/add

## Technologies

- Python
- FastAPI
- Google Gemini API
- Sentence Transformers
- ChromaDB
- Pydantic
