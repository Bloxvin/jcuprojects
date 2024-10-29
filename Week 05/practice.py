
# 1. Percentage Change [Algorithm]
# get original_value
# get percentage_change
#
# result = original_value * percentage_change
# display original value, percentage change and result


# # 1. Percentage Change [ Code ]
# original_value = float(input("Original: "))
# percentage_change = float(input("Change: "))
# result = original_value*(1+percentage_change)
# print(f"Original: {original_value}, Change: {percentage_change}, Result: {result}")

# 2. Time of day [Algorithm]
#
# time_statement = ""
# action_statement = ""
#
# get time_of_day
# get action
#
# if time_of_day > 12
#     time_statement = "after noon"
# else
#     time_statement = "before_noon"
#
# if action == "coming"
#     action_statement = "coming. Hi!"
# else
#     action_statement = "going. Bye!"
#
# display situation

# 2. Time of day {Code}
# time_statement = ""
# action_statement = ""
#
# time_of_day = int(input("Time of day: "))
# action = input("Action (coming or going): ")
#
# if time_of_day > 12:
#     time_statement = "after noon"
# else:
#     time_statement = "before noon"
#
# if action == "coming":
#     action_statement = "coming. Hi!"
# else:
#     action_statement = "going. Bye!"
#
# print(f"It is {time_statement} and you are {action_statement}")
#
# 3. Coffee Orders [ Algorithm ]
# get coffee
# get size
# cost = 0
#
# if size == "small"
#     cost = 3
# elif size == "medium"
#     cost = 4
# else
#     cost = 5
#
# if coffee != "black"
#     cost += 1
#
# display cost

# # 3. Coffee Orders [ Code ]
# coffee = input("Select Coffee Type [ White or Black ]: ").lower()
# size = input("Select Size [ Small or Medium or Large ]: ").lower()
# if size == "small":
#     cost = 3
# elif size == "medium":
#     cost = 4
# else:
#     cost = 5
#
# if coffee != "black":
#     cost += 1
#
# print(f"a {coffee} {size} coffee would cost {cost}.")
#
# Repetition Structures
# 4. Coffee orders with error-checking [Algorithm]
#
# get coffee
# while coffee != "black" or coffee != "white"
#     display Invalid coffee
#     get coffee
#
# get size
# while size != "small" or size != "medium" or size != "large"
#     display Invalid size
#     get size
# cost = 0
#
# if size == "small"
#     cost = 3
# elif size == "medium"
#     cost = 4
# else
#     cost = 5
#
# if coffee != "black"
#     cost += 1
#
# display cost

# # Coffee Orders [ Code ]
# coffee = input("Select Coffee Type [ White or Black ]: ").lower()
# while coffee != "black" and coffee != "white":
#     print("Invalid coffee")
#     coffee = input("Select Coffee Type [ White or Black ]: ").lower()
#
# size = input("Select Size [ Small or Medium or Large ]: ").lower()
# while size != "small" and size != "medium" and size != "large":
#     print("Invalid size")
#     size = input("Select Size [ Small or Medium or Large ]: ").lower()
#
# cost = 0
#
# if size == "small":
#     cost = 3
# elif size == "medium":
#     cost = 4
# else:
#     cost = 5
#
# if coffee != "black":
#     cost += 1
#
# print(f"a {coffee} {size} coffee would cost {cost}.")

# 5. Accumulation [Algorithm]
# total = 0
# get low_value
# get high_value
# while high_value <= low_value
#     display Invalid high value
#     get high_value
#
# for value in range(low_value, high_value+1)
#     display value
#     total += value
#
# display total

# 5. Accumulation [Code]
# total = 0
# low_value = int(input("Low value: "))
# high_value = int(input("High value: "))
# while high_value <= low_value:
#     print("Invalid high value.")
#     high_value = int(input("High value: "))
#
# for value in range(low_value, high_value+1):
#     print(value, end=" ")
#     total += value
#
# print(f"totals: {total}")

# 6. Debugging [Code] <- Algorithm not needed since debugging code
#
# age = int(input("Age: "))
# if age < 18:
#     print("Entry refused")
# elif age < 30:
#     print("Limited entry allowed")
# elif age >= 30:
#     print("Full entry allowed")

# Test values:17, 18, 29, 30, 31
# (Input and expected outcomes)
# ...
# Improved code: in line 221, age > 30 changed to age >= 30
