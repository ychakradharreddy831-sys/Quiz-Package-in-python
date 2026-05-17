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

 Clone the repository

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


<img width="630" height="798" alt="Screenshot 2026-05-17 011614" src="https://github.com/user-attachments/assets/2d2780fd-2b35-4189-a75b-eb7f271a68f4" />


<img width="667" height="851" alt="Screenshot 2026-05-17 011643" src="https://github.com/user-attachments/assets/b410fe6d-adde-4adf-85a1-cc1391732525" />


<img width="750" height="194" alt="Screenshot 2026-05-17 011659" src="https://github.com/user-attachments/assets/96d4c507-26da-4566-bda9-672302eefd95" />




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

