from PyPDF2 import PdfReader

def read_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text.strip()

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().strip()
