import chromadb

def get_chroma_collection():
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="my_collection")
    return collection

def save_to_chroma(collection, chunks, source_name):
    ids = [f"{source_name}_{i}"
           for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        ids=ids,
        metadatas=[{"source": source_name} for _ in chunks]
    )

if __name__ == "__main__":
    from ingestion import extract_text_from_pdf, chunk_text

import chromadb

def get_chroma_collection():
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="my_collection")
    return collection

def save_to_chroma(collection, chunks, source_name):
    ids = [f"{source_name}_{i}"
           for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        ids=ids,
        metadatas=[{"source": source_name} for _ in chunks]
    )

if __name__ == "__main__":
    from ingestion import extract_text_from_pdf, chunk_text

    with open("test_files/testing-2.pdf", "rb") as f:
        text = extract_text_from_pdf(f.read())
    chunks = chunk_text(text)

    collection = get_chroma_collection()
    save_to_chroma(collection, chunks, "testing-2.pdf")
    print(collection.count())