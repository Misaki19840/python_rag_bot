import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FAISSRetriever:
    def __init__(self, corpus_path: str):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.corpus = self._load_corpus(corpus_path)
        self.index = self._build_index()

    def _load_corpus(self, path: str):
        with open(path, encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]

    def _build_index(self):
        embeddings = self.embedder.encode(self.corpus, convert_to_tensor=False)
        dim = len(embeddings[0])
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings))
        self.embeddings = embeddings  # for reference
        return index

    def query(self, question: str, top_k=3):
        query_embedding = self.embedder.encode([question])[0]
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return [self.corpus[i] for i in I[0]]
