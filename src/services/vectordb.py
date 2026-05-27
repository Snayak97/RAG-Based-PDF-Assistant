import chromadb

# Create Chroma client
client = chromadb.Client()
client = chromadb.PersistentClient(
    path="../db/chroma_db"
)

# Create collection
collection = client.get_or_create_collection(
    name="rag_collection"
)


def store_chunks(chunks, embeddings):

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            ids=[str(i)]
        )


def search_chunks(query_embedding, n_results=3):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        # query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results