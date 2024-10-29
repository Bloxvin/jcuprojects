"""
function print shape(number)
    for i in range(number)
        print i*"*"
"""
MINIMAL_SCORE = 0
MAXIMUM_SCORE = 100

def print_shape(number):
    for i in range(number+1):
        print(i*"*")

def get_valid_score(prompt):
    score = float(input(prompt))
    while score < MINIMAL_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input(prompt))
    return score

def main():
    python_score = get_valid_score("Enter python score: ")
    database_score = get_valid_score("Enter database score: ")
    print("Python score:",python_score)
    print("Database score:",database_score)

main()