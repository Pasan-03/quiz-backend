# Fetch quizzes for a specific subject
subject = "CS"
quizzes = quizzes_collection.find({"subject": subject})

# Display results
for quiz in quizzes:
    print(quiz)


