
from google import genai
from google.genai import types

from app.config import settings


class EmbeddingService:
    def __init__(self):
        if not settings.gemini_api_key:
            raise ValueError("GEMINI_API_KEY is not configured")

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.embedding_model

    def encode(
        self,
        texts: list[str],
        task_type: str = "RETRIEVAL_QUERY",
        titles: list[str] | None = None
    ):
        if not texts:
            return []

        if titles is not None and len(titles) != len(texts):
            raise ValueError("Number of titles must match number of texts")

        vectors = []

        for index, text in enumerate(texts):
            config_args = {
                "task_type": task_type
            }

            if task_type == "RETRIEVAL_DOCUMENT":
                title = (
                    titles[index]
                    if titles
                    else "BugPilot knowledge document"
                )
                config_args["title"] = title

            response = self.client.models.embed_content(
                model=self.model,
                contents=text,
                config=types.EmbedContentConfig(**config_args)
            )

            vectors.append(
                response.embeddings[0].values
            )

        return vectors


embedding_service = EmbeddingService()
