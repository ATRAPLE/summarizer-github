import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

from .chunking import chunk_text
from .summarize import summarize_chunks

load_dotenv()

app = FastAPI()

SUPPORTED_MODELS = [
    "gpt-oss:20b",
    "gpt-oss:120b",
    "qwen3:30b",
    "qwen3:235b"
]

@app.post("/summarize", response_class=PlainTextResponse)
def summarize_pdf(
    file: UploadFile = File(...),
    model: str = Form("gpt-oss:20b"),
    chunk_chars: int = Form(450000),
    overlap: int = Form(0)
):
    if model not in SUPPORTED_MODELS:
        raise HTTPException(status_code=400, detail=f"Modelo não suportado: {model}")

    # Salvar PDF temporariamente
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(file.file.read())

    # Extrair texto do PDF (placeholder)
    text = "PDF extraction not implemented"
    # TODO: implementar extração real

    # Chunking
    chunks = chunk_text(text, chunk_size=chunk_chars, overlap=overlap)
    result = summarize_chunks([c for c, _ in chunks])
    return result
