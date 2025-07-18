from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List, Dict, Any, Literal
from pydantic import BaseModel, Field

router = APIRouter()

class QuizConfig(BaseModel):
    question_types: Literal['Multiple Choice', 'True/False', 'Fill in the blank', 'Identification', 'Multiple Answers', 'Mixed']
    difficulty: Literal['Easy', 'Medium', 'Hard']
    total_number_of_questions: int
    random_order: bool

@router.post('/generate/questions/')
async def generate_questions(lesson: str, quiz_config: QuizConfig):
    pass