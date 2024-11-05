""""
CP 1401 Practical 6
Kaung Myat Kyaw

[[[[[ Calculate salary for worker level ]]]]]
[ Algorithm ]
========================================
#

function main()
    worker_level = get_valid_level("Level", 1, 10)
    salary = calculate_salary(worker_level)
    print worker_level, salary

function get_valid_level(prompt, low, high)
    get level
    while level < low or level > high
        print Invalid
        get level
    return level

function calculate_salary_from_level(level)
    return level * 5000

main()
================================

[ Code ]
#
"""

def main():
    worker_level = get_valid_level("Level: ", 1, 10)
    salary = calculate_salary_from_level(worker_level)
    print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")

def get_valid_level(prompt, low, high):
    level = int(input(prompt))
    while level < low or level > high:
        print("Invalid")
        level = int(input(prompt))
    return level

def calculate_salary_from_level(level):
    return level * 5000

main()
"""
CP 1401 Practical 06
Print Grid Previous Prac Rewritten to Functions

================ [ Algorithm ] ========================
#

function main()
    get rows
    get columns
    print_grid(rows, columns)
    
function print_grid(rows, columns)  
    for row_number in range(rows)
        for column_number in range(columns)
            display column_number
        go next line
        
main()

================= [ Code ] ============================
"""

def main():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    print_grid(rows, columns)

def print_grid(rows, columns):
    for row_number in range(rows):
        for column_number in range(columns):
            print(column_number, end=" ")
        print()

main()

