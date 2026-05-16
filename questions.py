# ==========================================
# File: quizapp/questions.py
# ==========================================

questions_data = [
    {
        "question": "What is the capital of India?",
        "options": [
            "A. Chennai",
            "B. New Delhi",
            "C. Mumbai",
            "D. Kolkata"
        ],
        "answer": "B"
    },
    {
        "question": "Which language is used for Python development?",
        "options": [
            "A. Java",
            "B. C++",
            "C. Python",
            "D. HTML"
        ],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Primary Unit",
            "C. Central Program Utility",
            "D. Core Process Unit"
        ],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "A. define",
            "B. function",
            "C. def",
            "D. func"
        ],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "A. //",
            "B. <!-- -->",
            "C. #",
            "D. **"
        ],
        "answer": "C"
    }
]


def show_questions():
    print("\n========== QUIZ ==========")

    for index, question in enumerate(questions_data, start=1):

        print(f"\nQuestion {index}:")
        print(question["question"])

        for option in question["options"]:
            print(option)


def get_question(index):

    if 0 <= index < len(questions_data):
        return questions_data[index]

    return None