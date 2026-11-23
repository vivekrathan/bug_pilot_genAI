
from app.retrieval import retrieve_similar_issues
from app.gemini_client import gemini_service


def analyze_bug_report(bug_report: dict):
    similar_issues = retrieve_similar_issues(bug_report)

    gemini_result = gemini_service.analyze_bug(
        bug_report=bug_report,
        retrieved_issues=similar_issues
    )

    return {
        **gemini_result,
        "similar_issues": similar_issues
    }
