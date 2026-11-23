
SAMPLE_KNOWLEDGE = [
    {
        "id": "bug-001",
        "title": "Database connection timeout",
        "content": """
        Application fails while connecting to the database.
        Error: connection timed out.
        Possible causes include database server overload,
        incorrect connection configuration, network problems,
        exhausted connection pools, or firewall restrictions.
        Check database availability, host and port, connection
        pool size, network connectivity, and timeout settings.
        """,
        "source": "sample-knowledge-base",
        "component": "database"
    },
    {
        "id": "bug-002",
        "title": "Null pointer exception",
        "content": """
        Application crashes with a NullPointerException.
        This can happen when code accesses a method or property
        on a null object. Inspect the stack trace, identify the
        first application-owned line, and check whether the
        object is initialized before use. Validate inputs and
        add appropriate null checks.
        """,
        "source": "sample-knowledge-base",
        "component": "backend"
    },
    {
        "id": "bug-003",
        "title": "HTTP 500 internal server error",
        "content": """
        API returns HTTP 500. This indicates an unexpected
        server-side failure. Inspect application logs and
        stack traces, reproduce the request, check recent
        deployments, validate database queries and external
        service responses, and identify the failing operation.
        """,
        "source": "sample-knowledge-base",
        "component": "api"
    },
    {
        "id": "bug-004",
        "title": "Frontend application not loading",
        "content": """
        Web page displays a blank screen or fails to load.
        Possible causes include JavaScript runtime errors,
        failed API requests, incorrect environment variables,
        missing assets, routing errors, or build failures.
        Inspect browser developer console and network tab.
        """,
        "source": "sample-knowledge-base",
        "component": "frontend"
    },
    {
        "id": "bug-005",
        "title": "Authentication token expired",
        "content": """
        Users receive unauthorized responses after login.
        Possible causes include expired JWT tokens, incorrect
        token validation, clock differences, invalid signing
        keys, or refresh token failures. Inspect token expiry,
        authentication middleware, and refresh logic.
        """,
        "source": "sample-knowledge-base",
        "component": "authentication"
    },
    {
        "id": "bug-006",
        "title": "Memory usage continuously increases",
        "content": """
        Application memory usage increases over time.
        Possible causes include memory leaks, unclosed
        resources, retained object references, unbounded
        caches, or background tasks. Inspect memory profiles,
        resource cleanup, and long-running processes.
        """,
        "source": "sample-knowledge-base",
        "component": "performance"
    },
    {
        "id": "bug-007",
        "title": "API request returns 404",
        "content": """
        API endpoint returns 404 Not Found. Check the request
        URL, HTTP method, route registration, API prefix,
        reverse proxy configuration, and deployment version.
        Confirm that the requested resource exists.
        """,
        "source": "sample-knowledge-base",
        "component": "api"
    },
    {
        "id": "bug-008",
        "title": "Database query is very slow",
        "content": """
        Database queries take a long time to execute.
        Possible causes include missing indexes, inefficient
        joins, large table scans, excessive database calls,
        or poor query plans. Inspect query execution plans,
        indexes, database metrics, and query patterns.
        """,
        "source": "sample-knowledge-base",
        "component": "database"
    }
]
