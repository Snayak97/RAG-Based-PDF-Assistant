from fastapi import FastAPI
from api.rag import router as rag_router

app = FastAPI()

# Register API routes
app.include_router(rag_router)


@app.get("/")
def home():
    return {"message": "RAG Backend Running"}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8002)
