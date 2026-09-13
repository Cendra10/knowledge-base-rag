import io
from pypdf import PdfReader
from docx import Document

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

with open("test_files/testing-2.pdf", "rb") as f:
    file_bytes = f.read()

text = extract_text_from_pdf(file_bytes)
chunks = chunk_text(text)

print(len(chunks))
print(chunks[0])