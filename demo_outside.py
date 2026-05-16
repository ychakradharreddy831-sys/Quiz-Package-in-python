# ==========================================
# File: demo_outside.py
# ==========================================

from quizapp import (
    show_questions,
    get_question,
    evaluate_all,
    calculate_score,
    show_result
)


def main():

    show_questions()

    answers = []

    total_questions = 5

    for i in range(total_questions):

        while True:

            answer = input(
                f"\nEnter answer for Question {i + 1} (A/B/C/D): "
            ).upper()

            if answer in ["A", "B", "C", "D"]:
                answers.append(answer)
                break

            else:
                print("Invalid input! Please enter A/B/C/D only.")

    results = evaluate_all(answers)

    score = calculate_score(results)

    show_result(score, total_questions)

    print("\n========== ANSWER REVIEW ==========")

    for i, result in enumerate(results):

        question = get_question(i)

        print(f"\nQuestion {i + 1}: {question['question']}")

        if result:
            print("Your Answer : Correct")
        else:
            print(
                f"Correct Answer : {question['answer']}"
            )


if __name__ == "__main__":
    main()