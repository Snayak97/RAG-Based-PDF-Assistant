from services.parser import parse_pdf
from services.embeddings import generate_embedding
from services.vectordb import store_chunks, search_chunks
from services.llm import generate_answer


def process_pdf(pdf_path: str):

    # Parse + chunk
    chunks = parse_pdf(pdf_path)

    # Generate embeddings
    embeddings = generate_embedding(chunks)

    # Store in vector DB
    store_chunks(chunks, embeddings)

    return {
        "total_chunks": len(chunks)
    }


def ask_question(question):

    # Create question embedding
    query_embedding = generate_embedding(question)

    # Search similar chunks
    results = search_chunks(query_embedding)

    print("RETRIEVED RESULTS:")
    print(results)

    # Extract documents
    documents = results["documents"][0]

    # Combine context
    context = "\n\n".join(documents)

    print("CONTEXT:")
    print(context)

    # Create prompt
    prompt = f"""
You are an AI PDF assistant.

Answer ONLY using the provided context.

RULES:
- Extract the most relevant information from context
- Preserve bullet points and formatting when possible
- Do NOT invent information
- Do NOT use outside knowledge
- If exact answer is unavailable, return the closest relevant content from context
- Only say "Answer not found in document" if context is completely unrelated

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    print("FINAL PROMPT:")
    print(prompt)

    # Generate answer
    answer = generate_answer(prompt)

    print("FINAL ANSWER:")
    print(answer)

    if (
        "not found" in answer.lower()
        and len(documents) > 0
    ):

        print("USING FALLBACK CHUNK")

        answer = documents[0]


    return {
        "question": question,
        "answer": answer,
        "context": documents
    }