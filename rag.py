from dotenv import load_dotenv
from openai import OpenAI
import os
from embeddings import get_chroma_collection

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def retrieve_chunks(collection, question, n_results=3):
    query_results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    return query_results['documents'][0]

def ask_rag(collection, question):
    chunks = retrieve_chunks(collection, question)
    context = "\n".join(chunks)
    prompt = [{
        "role": "system",
        "content": "jawab HANYA berdasarkan context dan menjawab singkat dalam Bahasa Indonesia."
    }]
    prompt.append({
        "role": "user", 
        "content": f"Context:\n{context}\n\nPertanyaan: {question}"
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=prompt
    )

    return response.choices[0].message.content

collection = get_chroma_collection()
answer = ask_rag(collection, "apa itu project ini")
print(answer)