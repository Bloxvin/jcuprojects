"""
CP 1401, Kaung Myat Kyaw
Algorithm:
2. Parity.py
"""
from token import NUMBER

"""
[ Part 1 ]

function main()
    print calculate_parity(4)
    print calculate_parity(41)
    
    get number
    parity = calculate_parity(number)
    print parity
    
    if is_odd(number)
        print The number is odd
    else 
        print The number is even

function print_parity(number)
    parity = number % 2
    print parity

function calculate_parity(number)
    parity = number % 2
    return parity
    
function is_odd(number)
    if number % 2 == 0
        return False
    return True
"""

def main():
    print_parity(4)
    print_parity(41)

    number = int(input("Number: "))
    parity = calculate_parity(number)
    print(parity)

    if is_odd(number):
        print("The number is odd")
    else:
        print("The number is even")

def print_parity(number):
    parity = number % 2
    print(parity)

def calculate_parity(number):
    parity = number % 2
    return parity

def is_odd(number):
    if number % 2 == 0:
        return False
    return True

main()

