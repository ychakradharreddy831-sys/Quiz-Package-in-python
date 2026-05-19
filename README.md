# Quiz-Package-in-python 

QuizApp (Python Console Quiz Application)

---->Overview

QuizApp is a simple Python-based console quiz application designed for beginners who want to understand Python packages, modular programming, and user interaction through the command line.

The application asks multiple-choice questions (MCQs), validates user input, checks answers automatically, calculates the score, and displays the final percentage along with pass/fail status.

This project is fully developed using core Python without any external libraries, making it lightweight and easy to understand.

---->Features

Multiple-choice quiz system

Console-based interactive application

Input validation for user answers

Automatic answer checking

Score calculation

Percentage generation

Pass/Fail result display

Modular package structure

Beginner-friendly code

Easy to extend and customize

---->quiz_project/

│

├── quizapp/

│   ├── __init__.py

│   ├── questions.py

│   ├── evaluate.py

│   └── score.py

│

├── demo_outside.py

└── setup.py

---->Module Description

1. questions.py

This module stores all quiz questions and displays them to the user.

Responsibilities

Store MCQ questions

Store options (A/B/C/D)

Store correct answers

Display questions properly

2.evaluate.py

This module checks whether the user answer is correct or incorrect.

Responsibilities

Compare user answers

Validate answers

Return result status

3. score.py

This module calculates and displays the final quiz result.

Responsibilities

Calculate total marks

Calculate percentage

Display pass/fail result

4. demo_outside.py

This is the main file used to run the application.

Responsibilities

Import all modules

Start quiz execution

Handle quiz flow

Display final result


---->Requirements

Python 3.7 or higher

No external libraries required


---->Installation Guide

Step 1: Clone the Repository

git clone <repository-url>

Step 2: Move to Project Directory

cd quiz_project

Step 3: Run the Application

python demo_outside.py


----> How the Application Works

The program starts execution.

Quiz questions are displayed one by one.

User enters answers using:

A

B

C

D

Input is validated.

Answers are checked automatically.

Score is calculated.

Final percentage is displayed.

Pass/Fail status is shown.

---->Package Structure Explanation

The project follows a modular package structure.

Advantages

Better code organization

Easy maintenance

Reusable modules

Easy debugging

Professional coding practice

---->Concepts Used

This project demonstrates the following Python concepts:

Functions

Lists

Dictionaries

Loops

Conditional Statements

User Input

Modules

Packages

Import Statements

String Handling


----> Learning Objectives

This project helps beginners learn:

How Python packages work

How to split code into modules

How to create reusable functions

How to build console applications

How to manage project structure

---->Future Improvements

The project can be improved further by adding:

 Timer Feature

Add a timer for each question.

-----> Why This Project is Useful?

This project is ideal for:

Python beginners

College mini-projects

Practice projects

Learning modular programming

Understanding package creation

----> The version of pip is 

 26.1.1



 <img width="630" height="798" alt="Screenshot 2026-05-17 011614" src="https://github.com/user-attachments/assets/a5423d3e-d3fb-420f-bcaa-840688fa2e15" />




->Example Output


<img width="630" height="798" alt="Screenshot 2026-05-17 011614" src="https://github.com/user-attachments/assets/2d2780fd-2b35-4189-a75b-eb7f271a68f4" />


<img width="667" height="851" alt="Screenshot 2026-05-17 011643" src="https://github.com/user-attachments/assets/b410fe6d-adde-4adf-85a1-cc1391732525" />


<img width="750" height="194" alt="Screenshot 2026-05-17 011659" src="https://github.com/user-attachments/assets/96d4c507-26da-4566-bda9-672302eefd95" />



Author

Y.Chakradhar Reddy 

