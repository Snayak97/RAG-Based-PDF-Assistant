from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(texts:str):

    embeddings = model.encode(texts)

    return embeddings