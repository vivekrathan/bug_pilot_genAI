
from pydantic import BaseModel, Field
from typing import List, Optional


class BugReport(BaseModel):
    title: str = Field(..., min_length=3)
    description: str = Field(..., min_length=5)
    stack_trace: Optional[str] = ""
    environment: Optional[str] = ""
    component: Optional[str] = ""


class KnowledgeDocument(BaseModel):
    title: str
    content: str
    source: Optional[str] = "user-added"
    component: Optional[str] = "unknown"


class RetrievedIssue(BaseModel):
    id: str
    title: str
    content: str
    source: str
    similarity: float


class TriageResponse(BaseModel):
    summary: str
    severity: str
    severity_reason: str
    affected_subsystem: str
    root_cause_hypotheses: List[str]
    debugging_steps: List[str]
    suggested_fix: str
    similar_issues: List[RetrievedIssue]
    confidence: str
    limitations: List[str]
