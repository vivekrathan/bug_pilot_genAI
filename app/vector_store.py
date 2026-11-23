
import chromadb

from app.config import settings
from app.data import SAMPLE_KNOWLEDGE
from app.embeddings import embedding_service


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=settings.chroma_path
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, documents: list[dict]):
        if not documents:
            return

        existing = set(self.collection.get()["ids"])

        new_documents = [
            doc for doc in documents
            if doc["id"] not in existing
        ]

        if not new_documents:
            return

        texts = [
            f"{doc['title']}\n{doc['content']}"
            for doc in new_documents
        ]

        embeddings = embedding_service.encode(
            texts,
            task_type="RETRIEVAL_DOCUMENT",
            titles=[
                doc["title"] for doc in new_documents
            ]
        )

        self.collection.add(
            ids=[doc["id"] for doc in new_documents],
            documents=texts,
            embeddings=embeddings,
            metadatas=[
                {
                    "title": doc["title"],
                    "source": doc.get("source", "unknown"),
                    "component": doc.get("component", "unknown")
                }
                for doc in new_documents
            ]
        )

    def search(self, query: str, top_k: int = 4):
        collection_count = self.collection.count()

        if collection_count == 0:
            return []

        query_embedding = embedding_service.encode(
            [query],
            task_type="RETRIEVAL_QUERY"
        )[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=min(top_k, collection_count)
        )

        matches = []

        if not results["ids"] or not results["ids"][0]:
            return matches

        for index, document_id in enumerate(results["ids"][0]):
            metadata = results["metadatas"][0][index]
            distance = results["distances"][0][index]

            matches.append({
                "id": document_id,
                "title": metadata.get("title", "Untitled"),
                "content": results["documents"][0][index],
                "source": metadata.get("source", "unknown"),
                "component": metadata.get("component", "unknown"),
                "similarity": round(
                    max(0.0, 1.0 - distance), 4
                )
            })

        return matches


vector_store = VectorStore()


def initialize_knowledge_base():
    vector_store.add_documents(SAMPLE_KNOWLEDGE)
