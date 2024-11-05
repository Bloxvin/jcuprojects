"""
function main()
    subject_score = get_valid_score(prompt)
    final_result = determine_final_result(subject_score)
    display final_result

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

main()
"""
from PIL.ImImagePlugin import number
#
# MINIMUM_SCORE = 0
# MAXIMUM_SCORE = 100
# PASSING_SCORE = 50
# CREDIT_SCORE = 65
# DISTINCTION_SCORE = 75
# HIGH_DISTINCTION_SCORE = 85
#
# def main():
#     score = get_valid_score("Enter score: ")
#     result = determine_final_result(score)
#     print("Final result is",result)
#
# def get_valid_score(prompt):
#     score = float(input(prompt))
#     while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
#         print("Invalid score")
#         score = float(input(prompt))
#     return score
#
# def determine_final_result(score):
#     if score >= HIGH_DISTINCTION_SCORE:
#         result = "HD"
#     elif score >= DISTINCTION_SCORE:
#         result = "D"
#     elif score >= CREDIT_SCORE:
#         result = "C"
#     elif score >= PASSING_SCORE:
#         result = "P"
#     else:
#         result = "F"
#     return result
#
# main()

"""

function main()
    number_of_subjects = get_valid_number_of_subjects("How many subjects did you do? :")
    for subject in range(number_of_subjects)
        subject_code = get_valid_subject_code("Enter subject code: ")
        score = get_valid_score("Enter score: ")
        display subject_code & score
    
function get_valid_number_of_subjects(prompt)
    get number_of_subjects
    while number_of_subjects < 0 or number_of_subjects > 4
        display Invalid subject
        get number_of_subjects
    return number_of_subjects
    
function get_valid_subject_code(prompt)
    get subject_code
    while subject_code < 0 or subject_code > 10000
        display Invalid subject_code
        get subject_code
    return subject_code

function get_valid_score(prompt)
    get score
    while score < 0 or score > 100
        display Invalid score
        get score
    return score

"""

MIN_NUMBER_OF_SUBJECTS = 0
MAX_NUMBER_OF_SUBJECTS = 4
MIN_SUBJECT_LENGTH = 6
MIN_SCORE = 0
MAX_SCORE = 100

def main():
    number_of_subjects = get_valid_number_of_subjects("Number of subjects: ")
    for subject in range(number_of_subjects):
        subject_code = get_valid_subject_code("Subject code: ")
        score = get_valid_score("Score: ")
        print("Subject code:",subject_code,"| Score:",score)

def get_valid_number_of_subjects(prompt):
    number_of_subjects = int(input(prompt))
    while number_of_subjects < MIN_NUMBER_OF_SUBJECTS or number_of_subjects > MAX_NUMBER_OF_SUBJECTS:
        print("Invalid subject")
        number_of_subjects = int(input(prompt))
    return number_of_subjects

def get_valid_subject_code(prompt):
    subject_code = input(prompt)
    while len(subject_code) < MIN_SUBJECT_LENGTH:
        print("Invalid subject code")
        subject_code = input(prompt)
    return subject_code

def get_valid_score(prompt):
    score = float(input(prompt))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = float(input(score))
    return score

main()

#
#
# import random
# random_no = random.randint(1,10)
# print(random_no)

