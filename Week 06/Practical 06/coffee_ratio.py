"""
CP 1401, Kaung Myat Kyaw
Algorithm:
1. Coffee Brew Ratio

[First Algorithm]
===================================
function determine_coffee_style(ratio)
    if dose > 20
        return "lungo"
    else if dose > 1.5
        return "normale"
    else
        return "ristretto"

[Second Algorithm]
===================================

function main()
    yield = get_valid_number("Yield:", 0, 1000)
    weight = get_valid_number("Dose:", 0, 1000)
    ratio = calculate_ratio(yield, weight)
    style = determine_coffee_style(ratio)
    print ratio, style

function determine_coffee_style(ratio)
    if ratio > 20
        return "lungo"
    else if ratio > 1.5
        return "normale"
    else
        return "ristretto"

function get_valid_number(prompt, low, high)
    print prompt
    get number
    while number < low or number > high
        print error, prompt
        get number
    return number

function calculate_ratio(dose, yield)
    ratio = yield / dose
    return ratio

"""

def main():
    coffee_yield = get_valid_number("Yield: ", 0, 1000)
    brew = get_valid_number("Brew: ", 0, 1000)
    ratio = calculate_ratio(coffee_yield, brew)
    style = determine_coffee_style(ratio)
    print(f"1:{ratio:.2f} is considered {style}")

def determine_coffee_style(ratio):
    if ratio > 20:
        return "lungo"
    elif ratio > 1.5:
        return "normale"
    else:
        return "ristretto"

def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid number")
        number = float(input(prompt))
    return number

def calculate_ratio(dose, coffee_yield):
    ratio = coffee_yield/dose
    return ratio

main()