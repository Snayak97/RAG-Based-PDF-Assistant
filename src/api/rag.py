from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os

from services.rag_service import (
    process_pdf,
    ask_question
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = process_pdf(file_path)

    return {
        "message": "PDF processed successfully",
        "filename": file.filename,
        "total_chunks": result["total_chunks"]
    }


@router.post("/ask")
def ask(request: QuestionRequest):

    result = ask_question(request.question)

    return result