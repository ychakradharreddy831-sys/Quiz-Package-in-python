# Quiz-Package-in-python
QuizApp (Python Console Quiz Application)

A simple Python-based Quiz Application that runs in the console.
It asks multiple-choice questions, evaluates user answers, and displays the final score with pass/fail status.

Features
Multiple-choice questions (MCQ format)
Input validation (A / B / C / D only)
Automatic answer checking
Score calculation
Percentage result
Pass / Fail status
Modular Python package structure
Project Structure
quiz_project/
│
├── quizapp/
│   ├── __init__.py
│   ├── questions.py
│   ├── evaluate.py
│   └── score.py
│
├── demo_outside.py
└── setup.py
How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/quizapp.git
cd quizapp
Run the application
python demo_outside.py
How It Works
1.The program displays quiz questions
2.User enters answers (A / B / C / D)
3.Answers are checked automatically
4.Score is calculated
5.Final result is shown with percentage
Example Output
===== QUIZ =====

Question 1:
What is the capital of India?
A. Chennai
B. New Delhi
C. Mumbai
D. Kolkata

Enter answer for Question 1 (A/B/C/D): B

===== RESULT =====
Score: 3/5
Percentage: 60.00%
Status: PASS
Modules Explained
questions.py

Stores all quiz questions and displays them.

evaluate.py

Checks user answers against correct answers.

score.py

Calculates score and displays final result.

demo_outside.py

Main file that runs the quiz application.

Requirements
Python 3.7+

No external libraries required.

Future Improvements
Add timer for each question 
GUI version using Tkinter or PyQt 
Database integration for storing scores 
Random question shuffle 
User login system

Author
Y.Chakradhar Reddy 

Python Developer | Beginner Project
