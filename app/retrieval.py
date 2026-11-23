
from app.config import settings
from app.vector_store import vector_store


def retrieve_similar_issues(bug_report: dict):
    query = f"""
    Title: {bug_report.get('title', '')}

    Description: {bug_report.get('description', '')}

    Stack trace: {bug_report.get('stack_trace', '')}

    Environment: {bug_report.get('environment', '')}

    Component: {bug_report.get('component', '')}
    """

    return vector_store.search(
        query=query,
        top_k=settings.top_k
    )
