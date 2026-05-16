# ==========================================
# File: quizapp/evaluate.py
# ==========================================

from .questions import questions_data


def check_answer(user_answer, correct_answer):

    return user_answer.strip().upper() == correct_answer.strip().upper()


def evaluate_all(user_answers):

    results = []

    for index, answer in enumerate(user_answers):

        correct_answer = questions_data[index]["answer"]

        result = check_answer(answer, correct_answer)

        results.append(result)

    return results