PROJECT STRUCTURE


rag_project/
│
├── src/
│   ├── main.py
│   │
│   ├── api/
│   │    └── rag.py
│   │
│   ├── services/
│   │    ├── parser.py
│   │    ├── embeddings.py
│   │    ├── vectordb.py
│   │    ├── llm.py
│   │    └── rag_service.py
│
├── ui/
│    └── app.







SYSTEM FLOW 
RAG pipeline is:

PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Question Embedding
 ↓
Similarity Search
 ↓
Retrieved Context
 ↓
LLM
 ↓
Final Answer



<!-- cmd to run -->
uv init
cd project name
uv venv
.venv\Scripts\activate

uv add -r requirements.txt

<!-- backend -->
python src/main.py

<!-- frontend -->
uv run streamlit run ui/app.py