
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import (
    BugReport,
    KnowledgeDocument,
    TriageResponse
)
from app.analyzer import analyze_bug_report
from app.vector_store import (
    initialize_knowledge_base,
    vector_store
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing BugPilot knowledge base...")

    initialize_knowledge_base()

    print(
        f"Knowledge base ready: "
        f"{vector_store.collection.count()} documents"
    )

    yield


app = FastAPI(
    title="GenAI Bug Triage Assistant",
    description=(
        "A RAG-based software bug triage and root-cause "
        "analysis assistant powered by Gemini."
    ),
    version="2.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",

    
        "https://bug-pilot-gen-ai.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "GenAI Bug Triage Assistant is running",
        "docs": "/docs",
        "features": [
            "Gemini-powered bug analysis",
            "RAG-based knowledge retrieval",
            "Similar issue search",
            "Root-cause hypotheses",
            "Debugging recommendations"
        ]
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "knowledge_documents": vector_store.collection.count()
    }


@app.post("/triage", response_model=TriageResponse)
def triage_bug(report: BugReport):
    try:
        result = analyze_bug_report(report.model_dump())
        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"Bug analysis failed: {str(error)}"
        )


@app.post("/knowledge/add")
def add_knowledge(document: KnowledgeDocument):
    try:
        import uuid

        vector_store.add_documents([
            {
                "id": uuid.uuid4().hex,
                "title": document.title,
                "content": document.content,
                "source": document.source,
                "component": document.component
            }
        ])

        return {
            "message": "Knowledge document added successfully",
            "total_documents": vector_store.collection.count()
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Could not add knowledge: {str(error)}"
        )
