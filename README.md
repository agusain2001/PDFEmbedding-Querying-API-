# 📄 PDF Embedding & Querying API  

A FastAPI-based service for processing PDF files, generating embeddings using Google's Generative AI, and enabling semantic search with FAISS.

---

## 🚀 Features  

- ✅ Extract text from PDF files  
- ✅ Split text into smaller chunks  
- ✅ Generate embeddings using Google's Generative AI  
- ✅ Store embeddings in a FAISS vector database  
- ✅ Perform semantic search on uploaded PDFs  
- ✅ FastAPI-based endpoints for easy interaction  

---

## 📂 Project Structure  

```
pdf_embedding_project/
│── main.py              # FastAPI app
│── embeddings.py        # Handles embedding generation
│── database.py          # FAISS vector database handling
│── pdf_processing.py    # PDF text extraction
│── config.py            # Configuration and environment variables
│── requirements.txt     # Dependencies
│── .env                 # Environment variables
│── README.md            # Setup Guide
```

---

## 🛠️ Setup & Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/agusain2001/PDFEmbedding-Querying-API-.git
cd pdf_embedding_project
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)  
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure API Key  
Create a `.env` file in the project root directory and add:  
```ini
GEMINI_API_KEY=your_google_api_key_here
```

---

## 🚀 Running the FastAPI Server  
Once everything is set up, run the FastAPI server with:  
```sh
python main.py
```

The server will be accessible at:  
🔗 [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 🔥 API Endpoints  

### 1️⃣ Upload a PDF  
**Endpoint:** `POST /upload`  
**Description:** Uploads a PDF file, extracts text, generates embeddings, and stores them in FAISS.  

#### Request Example  
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@example.pdf'
```

#### Response Example  
```json
{
    "message": "PDF processed successfully",
    "chunks": 12
}
```

---

### 2️⃣ Query the PDF  
**Endpoint:** `POST /query`  
**Description:** Perform a semantic search on the uploaded PDF and retrieve the most relevant chunks.  

#### Request Example  
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=What is the summary of the document?'
```

#### Response Example  
```json
{
    "answer": "The document explains the history of AI and its impact on society...",
    "context_chunks": [2, 5, 8]
}
```

---

## 🛠️ How It Works  

1️⃣ The `/upload` endpoint extracts text from a PDF, splits it into chunks, and generates embeddings using Google's Generative AI.  
2️⃣ The embeddings are stored in a FAISS vector database for efficient search.  
3️⃣ The `/query` endpoint converts a user’s query into an embedding and finds the most relevant chunks using FAISS similarity search.  

---

## 📌 Technologies Used  

- 🔹 **FastAPI** - Web framework for API development  
- 🔹 **FAISS** - Vector search database for fast retrieval  
- 🔹 **Google Generative AI** - Embeddings for semantic search  
- 🔹 **PyPDF2** - Extracting text from PDF files  
- 🔹 **NumPy** - Handling numerical computations  
- 🔹 **Python dotenv** - Managing environment variables  

---

## 🛡️ Security  

🔑 **API Key Management:** The API key is securely stored in the `.env` file and loaded via `config.py`.  
🔒 **Input Validation:** FastAPI automatically validates input types and formats.  

---


Made with ❤️ by Ashish Gusain 🚀

