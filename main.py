from fastapi import FastAPI
from schemas import AskRequest, AskResponse
from embeddings import get_chroma_collection
from ingestion import ingest_folder
from rag import ask_rag 

app = FastAPI()

@app.post("/ingest")
def ingest_endpoint():
    collection = get_chroma_collection()
    ingest_folder("data", collection)
    return {"message": "Ingestion complete", "total_chunks": collection.count()}

@app.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest):
    collection = get_chroma_collection()
    answer = ask_rag(collection, request.question)
    return AskResponse(answer=answer)

