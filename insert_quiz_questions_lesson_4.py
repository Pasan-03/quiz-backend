from pymongo import MongoClient

# MongoDB URI
mongo_uri = "mongodb+srv://donachinthapasan01:EoxpE2X83sE4Du1q@nextAuthDB.25ujz.mongodb.net/nextAuthDB?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Access the specific database and collection
db = client["nextAuthDB"]
quizzes_collection = db["quizzes"]

# Define the quiz questions with additional fields
quiz_questions = [
    {
        "syllabus": "Cambridge",
        "courseLevel": "GCSE",
        "subject": "CS",
        "topic": "introduction",
        "lesson_number": 4,
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
            {
                "questionText": "What is JavaScript?",
                "options": ["A programming language", "A markup language", "A style sheet language"],
                "correctAnswer": "A programming language"
            },
            {
                "questionText": "Which HTML element is used to define a header?",
                "options": ["<header>", "<head>", "<h1>"],
                "correctAnswer": "<header>"
            },
            {
                "questionText": "What is the correct HTML element for inserting a line break?",
                "options": ["<br>", "<break>", "<lb>"],
                "correctAnswer": "<br>"
            },
            {
                "questionText": "Which property is used to change the font of an element in CSS?",
                "options": ["font-family", "font-style", "text-style"],
                "correctAnswer": "font-family"
            },
            {
                "questionText": "What is the correct way to comment in CSS?",
                "options": ["// This is a comment", "/* This is a comment */", "<!-- This is a comment -->"],
                "correctAnswer": "/* This is a comment */"
            },
            {
                "questionText": "Which HTML element is used to define an unordered list?",
                "options": ["<ul>", "<ol>", "<li>"],
                "correctAnswer": "<ul>"
            },
            {
                "questionText": "What does API stand for?",
                "options": ["Application Programming Interface", "Application Programming Integration", "Application Program Interface"],
                "correctAnswer": "Application Programming Interface"
            },
            {
                "questionText": "Which HTML attribute specifies an alternate text for an image, if the image cannot be displayed?",
                "options": ["alt", "src", "title"],
                "correctAnswer": "alt"
            },
            {
                "questionText": "What is the purpose of the <title> element in HTML?",
                "options": ["Defines the title in the browser toolbar", "Creates a new section in the document", "Adds a heading to the page"],
                "correctAnswer": "Defines the title in the browser toolbar"
            },
            {
                "questionText": "Which CSS property controls the text color of an element?",
                "options": ["text-color", "font-color", "color"],
                "correctAnswer": "color"
            },
            {
                "questionText": "What does SQL stand for?",
                "options": ["Structured Query Language", "Sequential Query Language", "Simple Query Language"],
                "correctAnswer": "Structured Query Language"
            },
            {
                "questionText": "In HTML, how can you make a numbered list?",
                "options": ["<ul>", "<ol>", "<list>"],
                "correctAnswer": "<ol>"
            },
            {
                "questionText": "Which JavaScript keyword declares a variable?",
                "options": ["variable", "var", "declare"],
                "correctAnswer": "var"
            }
        ]
    }
]

# Insert questions into MongoDB collection
try:
    quizzes_collection.insert_many(quiz_questions)
    print("Sample quiz questions inserted successfully!")
except Exception as e:
    print("An error occurred:", e)

    # python insert_quiz_questions_lesson_4.py
