import faiss
import numpy as np

def build_faiss_index(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    """Build a FAISS vector index for fast search."""
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_index(index: faiss.IndexFlatL2, query_embedding: np.ndarray, k: int = 3):
    """Search FAISS index for the most relevant chunks."""
    distances, indices = index.search(query_embedding.reshape(1, -1), k)
    return indices[0], distances[0]
