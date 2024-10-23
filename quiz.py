from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import datetime

app = FastAPI()

client = MongoClient("mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority")
db = client["nextAuthDB"]
quiz_collection = db["quizzes"]

class QuizSubmission(BaseModel):
    user_id: str
    topic: str
    lesson_number: int
    answers: dict

@app.get("/quiz/{topic}/{lesson_number}")
async def get_quiz(topic: str, lesson_number: int):
    quiz = quiz_collection.find_one({"topic": topic, "lesson_number": lesson_number})
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@app.post("/quiz/submit")
async def submit_quiz(submission: QuizSubmission):
    quiz = quiz_collection.find_one({"topic": submission.topic, "lesson_number": submission.lesson_number})
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    correct_answers = quiz["questions"]
    score = sum(1 for question in correct_answers if submission.answers.get(question["question"]) == question["correct"])
    total_questions = len(correct_answers)
    percentage = (score / total_questions) * 100

    # Optionally save results
    return {"score": percentage, "total_questions": total_questions, "correct_answers": score}
