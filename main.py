from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import uvicorn

from pdf_processing import extract_text_from_pdf, split_text
from embeddings import get_embedding
from database import build_faiss_index, search_index

# Global variables for FAISS index and text chunks
global_index = None
global_chunks = None

app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """Endpoint to upload and process a PDF file."""
    global global_index, global_chunks

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    file_data = await file.read()
    
    try:
        text = extract_text_from_pdf(file_data)
        chunks = split_text(text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Generate embeddings and build FAISS index
    embeddings = np.array([get_embedding(chunk) for chunk in chunks])
    global_index = build_faiss_index(embeddings)
    global_chunks = chunks
    
    return JSONResponse(content={"message": "PDF processed successfully", "chunks": len(chunks)})

@app.post("/query")
async def query_pdf(query: str = Form(...)):
    """Endpoint to query the FAISS index and retrieve relevant information."""
    global global_index, global_chunks

    if not global_index or not global_chunks:
        raise HTTPException(400, "Upload PDF first")

    query_emb = get_embedding(query)
    indices, _ = search_index(global_index, query_emb)
    
    context = "\n".join([global_chunks[i] for i in indices])

    return JSONResponse({"answer": context, "context_chunks": indices.tolist()})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
