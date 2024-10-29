"""

function get_valid_score(prompt)
    get score
    if score < 0 or score > 100
        display invalid score
        get score
    return score

function determine_final_result(score)
    if score >= 85:
        result is HD
    else if score >= 75:
        result is D
    else if score >= 65:
        result is C
    else if score >= 50:
        result is P
    else:
        result is F
    return result

function main()
    subject_score = get_valid_score(prompt)
    final_result = determine_final_result(subject_score)
    display final_result

main()
"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSING_SCORE = 50
CREDIT_SCORE = 65
DISTINCTION_SCORE = 75
HIGH_DISTINCTION_SCORE = 85


def get_valid_score(prompt):
    score = float(input(prompt))
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input(prompt))
    return score

def determine_final_result(score):
    if score >= HIGH_DISTINCTION_SCORE:
        result = "HD"
    elif score >= DISTINCTION_SCORE:
        result = "D"
    elif score >= CREDIT_SCORE:
        result = "C"
    elif score >= PASSING_SCORE:
        result = "P"
    else:
        result = "F"
    return result

def main():
    score = get_valid_score("Enter score: ")
    result = determine_final_result(score)
    print("Final result is",result)

main()