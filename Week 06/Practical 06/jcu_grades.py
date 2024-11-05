"""
Practical 06 - CP 1401
3. JCU Grades

Algorithm


function main()
    get score
    while score > 0
        grade = calculate_grade(score)
        print score, grade
        get score

    number_of_random_scores = get_valid_number("Number of Random Scores: ", 0, 1000)
    for i in range(number_of_random_scores)
        random_score = get_random_integer(0,100)
        random_grade = calculate_grade(random_score)
        print random_score, random_grade



function get_valid_number(prompt, low)
    print prompt
    get number
    while number < low
        print Invalid
        get number
    return number

function calculate_grade(score)
    if score >= 85
        return "HD"
    elif score >= 75
        return "D"
    elif score >= 65
        return "C"
    elif score >= 50
        return "P"
    else
        return "F"

function get_random_integer(low, high)
    return random integer between low and high

main()
"""
import random
HIGHEST_SCORE = 100
LOWEST_SCORE = 0

def main():
    score = float(input("Score: "))
    while score > LOWEST_SCORE:
        grade = calculate_grade(score)
        print(f"The score {score} is {grade}")
        score = float(input("Score: "))

    number_of_random_scores = get_valid_number("How many random scores: ", 0)
    for i in range(number_of_random_scores):
        random_score = get_random_integer(LOWEST_SCORE,HIGHEST_SCORE)
        random_grade = calculate_grade(random_score)
        print(f"{random_score} = {random_grade}")


def get_valid_number(prompt, low):
    number = int(input(prompt))
    while number < low:
        print("Invalid")
        number = int(input(prompt))
    return number

def calculate_grade(score):
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "F"

def get_random_integer(low, high):
    return random.randint(low, high)

main()