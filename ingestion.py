import io
from pypdf import PdfReader
from docx import Document
from pathlib import Path
from embeddings import save_to_chroma, get_chroma_collection

def extract_text_from_pdf(pdf_bytes):
    page_list = []
    reader = PdfReader(io.BytesIO(pdf_bytes))

    for page in reader.pages:
        text = page.extract_text()
        page_list.append(text)

    return "\n".join(page_list)

def extract_text_from_docx(docx_bytes):
    doc = Document(io.BytesIO(docx_bytes))
    return "\n".join(p.text for p in doc.paragraphs)

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest_folder(folder_path, collection):
    for path in Path(folder_path).iterdir():
        file_bytes = path.read_bytes()

        if path.suffix == ".pdf":
            text = extract_text_from_pdf(file_bytes)
        elif path.suffix == ".docx":
            text = extract_text_from_docx(file_bytes)
        else:
            continue

        chunks = chunk_text(text)
        save_to_chroma(collection, chunks, path.name)


if __name__ == "__main__":
    collection = get_chroma_collection()
    ingest_folder("data", collection)
    print(collection.count())