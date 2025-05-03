from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class FAISSRetriever:
    def __init__(self, corpus_path: str):
        self.embedder = None
        self.index = None
        self.corpus = None
        self.corpus_path = corpus_path

    def load(self):
        if self.embedder is not None:
            return  # already loaded

        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

        with open(self.corpus_path, encoding='utf-8') as f:
            self.corpus = [line.strip() for line in f if line.strip()]

        embeddings = self.embedder.encode(self.corpus, convert_to_tensor=False)
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings))

    def query(self, question: str, top_k=3):
        self.load()  # lazy-load on first call
        query_embedding = self.embedder.encode([question])[0]
        _, I = self.index.search(np.array([query_embedding]), top_k)
        return [self.corpus[i] for i in I[0]]
