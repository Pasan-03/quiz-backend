from pymongo import MongoClient
from datetime import datetime

# MongoDB URI
mongo_uri = "mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority"  # Replace with your MongoDB URI
client = MongoClient(mongo_uri)

# Access the specific database
db = client["nextAuthDB"]

# Insert subject quiz
subject_quiz = {
    "syllabus": "Edexcel",
    "courseLevel": "GCSE",
    "subject": "ICT",
    "topic": "introduction",
    "questions": [
        {"questionText": "What does HTML stand for?", "options": ["Hypertext Markup Language", "Hightext Markup Language"], "correctAnswer": "Hypertext Markup Language"},
        {"questionText": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Creative Style Sheets"], "correctAnswer": "Cascading Style Sheets"}
    ],
    "created_at": datetime.utcnow(),
    "updated_at": datetime.utcnow()
}

# Insert lesson quiz
lesson_quiz = {
    "syllabus": "Cambridge",
    "courseLevel": "GCSE",
    "subject": "CS",
    "topic": "introduction",
    "lesson_number": 1,
    "questions": [
        {"questionText": "What does HTML stand for?", "options": ["Hypertext Markup Language", "Hightext Markup Language"], "correctAnswer": "Hypertext Markup Language"}
    ],
    "created_at": datetime.utcnow(),
    "updated_at": datetime.utcnow()
}

# Insert topic quiz
topic_quiz = {
    "syllabus": "Cambridge",
    "courseLevel": "GCSE",
    "subject": "CS",
    "topic": "introduction",
    "questions": [
        {"questionText": "What does HTML stand for?", "options": ["Hypertext Markup Language", "Hightext Markup Language"], "correctAnswer": "Hypertext Markup Language"}
    ],
    "created_at": datetime.utcnow(),
    "updated_at": datetime.utcnow()
}

# Insert into MongoDB
try:
    db.subjectQuizzes.insert_one(subject_quiz)
    db.lessonQuizzes.insert_one(lesson_quiz)
    db.topicQuizzes.insert_one(topic_quiz)
    print("Quizzes inserted successfully!")
except Exception as e:
    print("Error inserting quizzes:", e)
