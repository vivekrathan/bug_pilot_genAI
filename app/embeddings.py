
from sentence_transformers import SentenceTransformer
from app.config import settings


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(settings.embedding_model)

    def encode(self, texts: list[str]):
        vectors = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        return vectors.tolist()


embedding_service = EmbeddingService()
