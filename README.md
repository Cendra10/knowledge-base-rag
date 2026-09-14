# Knowledge Base RAG

## Description
A Retrieval-Augmented Generation (RAG) application that answers questions based on your own documents instead of relying only on the AI's general knowledge. Documents (PDF/DOCX) are processed into embeddings and stored in a vector database, then retrieved and injected as context whenever a relevant question is asked.

## Features
- Extract text from PDF and DOCX files
- Split documents into overlapping text chunks for better retrieval
- Generate embeddings locally (no external API cost) and store them in ChromaDB
- Automatically ingest all supported documents from a folder
- Retrieve the most relevant chunks for a given question (semantic search)
- Generate answers using an LLM based only on the retrieved context

## Tech Stack
- Python
- FastAPI
- ChromaDB (vector database)
- sentence-transformers (local embedding model)
- pypdf (PDF text extraction)
- python-docx (DOCX text extraction)
- OpenAI SDK (client library)
- Groq API (LLM provider, OpenAI-compatible)

## Installation
1. Clone the repository
```
git clone https://github.com/Cendra10/knowledge-base-rag.git
cd knowledge-base-rag
```
2. Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Create a `.env` file in the project root and add your Groq API key
```
GROQ_API_KEY=your_api_key_here
```

## Usage
1. Place your PDF or DOCX documents inside the `data/` folder.
2. Run ingestion to process and store documents in the vector database:
```
python ingestion.py
```
3. Ask questions based on the ingested documents:
```
python rag.py
```

## Project Structure
```
knowledge-base-rag/
    main.py                 # FastAPI endpoints (in progress)
    schemas.py              # Pydantic models
    ingestion.py            # Document loading, text extraction, chunking, folder ingestion
    embeddings.py           # ChromaDB connection and storage of embeddings
    rag.py                  # Retrieval and LLM answer generation
    data/                   # Documents to be ingested (not committed)
    chroma_db/              # Persistent vector database storage (not committed)
    config/
        config.py           # Environment variable config
    .env                    # API keys (not committed)
    .gitignore
    requirements.txt
    README.md
```

## Example
```
Question: apa itu project ini
Answer: Project ini merupakan proyek AI asisten yang dirancang untuk memproses,
menganalisis, dan membantu dalam mengelola file PDF.
```

## Future Improvement
- Expose ingestion and question-answering through FastAPI endpoints
- Support more file types (e.g. TXT, JSON)
- Add citation of source file/chunk in the answer
- Add automated tests
- Replace local embedding model with a higher-quality API-based model for production use (see Project 10)

## License
MIT License
