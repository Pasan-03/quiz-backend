from pymongo import MongoClient
from datetime import datetime

# MongoDB URI
mongo_uri = ""  # Replace with your actual MongoDB URI
client = MongoClient(mongo_uri)

# Access the specific database and collection
db = client["nextAuthDB"]
quizzes_collection = db["quizzes"]

# Define the quiz questions with additional metadata
quiz_questions = [
    {
        "syllabus": "Cambridge",
        "courseLevel": "GCSE",
        "subject": "CS",
        "topic": "Web Development Basics",
        "questions": [
            {
                "questionText": "What does HTML stand for?",
                "options": ["Hypertext Markup Language", "Hightext Markup Language", "Hypertext Machine Language"],
                "correctAnswer": "Hypertext Markup Language"
            },
            {
                "questionText": "What does CSS stand for?",
                "options": ["Cascading Style Sheets", "Creative Style Sheets", "Colorful Style Sheets"],
                "correctAnswer": "Cascading Style Sheets"
            },
            # Add more questions as needed...
        ],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
]

# Insert questions into MongoDB collection
try:
    quizzes_collection.insert_many(quiz_questions)
    print("Sample quiz questions inserted successfully!")
except Exception as e:
    print("An error occurred:", e)

# Fetch quizzes for a specific subject
subject = "CS"
quizzes = quizzes_collection.find({"subject": subject})

# Display results
for quiz in quizzes:
    print(quiz)
# python insert_subject_questions.py