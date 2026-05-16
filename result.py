# ==========================================
# File: quizapp/score.py
# ==========================================

def calculate_score(results):

    return sum(results)


def show_result(score, total):

    print("\n========== RESULT ==========")

    print(f"Total Score : {score}/{total}")

    percentage = (score / total) * 100

    print(f"Percentage  : {percentage:.2f}%")

    if percentage >= 50:
        print("Status      : PASS")
    else:
        print("Status      : FAIL")