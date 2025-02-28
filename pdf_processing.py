import io
import PyPDF2

def extract_text_from_pdf(file_data: bytes) -> str:
    """Extract text from a PDF file."""
    reader = PyPDF2.PdfReader(io.BytesIO(file_data))
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    
    if not text:
        raise ValueError("No text could be extracted from the PDF.")
    
    return text


def split_text(text: str, chunk_size: int = 100) -> list:
    """Split extracted text into smaller chunks."""
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
