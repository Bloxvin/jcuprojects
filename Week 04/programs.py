# ========== (1) Error Checking ==============
# [ Algorithm ]
# ========================================
# #
# get worker_level
# while worker_level < 1 or worker_level > 1
#     display error_message
#     get worker_level
#
# salary = worker_level * 5000
# display worker level & salary
# ========================================
# [ Code ]
# #
# worker_level = int(input("Worker Level: "))
# while worker_level < 1 or worker_level > 10:
#     print("Invalid Level.")
#     worker_level = int(input("Worker Level: "))
# salary = worker_level * 5000
# print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
# =========================================
# ===
#
# ============== (2) Number Sequences =================
# [ Algorithm ]
# ==========================================
# #
from mimetypes import guess_type
from random import choice

# a. for num in range(1,100,2)
#     display num
# b. for year in range(1896, 2024, 4)
#     display year
# c. for people in range(12)
#     display people
#     # display the number of people in a football team.
# ===========================================
# [ Code ]
# ==========================================
# #
# START_NUM = 1
# END_NUM = 100
# for num in range(START_NUM, END_NUM,2):
#     print(num)
#
# START_YEAR = 1896
# CURRENT_YEAR = 2024
# for year in range(START_YEAR, CURRENT_YEAR):
#     print(year)
#
# TOTAL_PEOPLE = 12
# for people in range(TOTAL_PEOPLE):
#     print(people)
#
# ============================================
# ============ (3) Menus =====================
# [ Algorithm ]
# # ============================================
# get statement
# while statement is not q
#     if statement is s
#         display :)
#     else if statement is f
#         display :(
#     else
#         display Invalid Choice
# display Farewell
# ===============================================
# [ Code ]
# ==============================================
# SMILE_STATEMENT = "s"
# FROWN_STATEMENT = "f"
# QUIT_STATEMENT = "q"
# ChoiceMenu = "(S)miley\n(F)rowny\n(Q)uit\n"
# statement = input(ChoiceMenu).lower()
#
# while statement != QUIT_STATEMENT:
#     if statement == SMILE_STATEMENT:
#         print(":)")
#     elif statement == FROWN_STATEMENT:
#         print(":(")
#     else:
#         print("Invalid choice")
#     statement = input(ChoiceMenu).lower()
# print("Farewell")
#=================================================
# =============== (4) Accumulation ===============
# ========== Average Age [ Algorithm ] =========================
# number_of_people = 0
# total_age = 0
# SENTINEL = -1
# get age
# while age != SENTINEL
#     number_of_people =+ 1
#     total_age = total_age + age
# average_age = total_age/number_of_people
# display average_age
#
# ==============================================
# ============ Average Age [ Code ] ============
# #
# number_of_people = 0
# total_age = 0
# SENTINEL = -1
# age = int(input("Age (-1 to stop): "))
# while age != SENTINEL:
#     number_of_people += 1
#     total_age = total_age + age
#     age = int(input("Age (-1 to stop): "))
# average_age = total_age/number_of_people
# print("Average age:",average_age)
# ============Smileys Count [Algorithm] ====================
# total_smile = 0
# total_frown = 0
# get statement
# while statement is not q
#     if statement is s
#         total_smile += 1
#         display :)
#     else if statement is f
#         total_frown += 1
#         display :(
#     else
#         display Invalid Choice
# display total_smile & total_frown
# ============= Smiley Count [ Code ] ======================
# SMILE_STATEMENT = "s"
# FROWN_STATEMENT = "f"
# QUIT_STATEMENT = "q"
# total_smile = 0
# total_frown = 0
# ChoiceMenu = "(S)miley\n(F)rowny\n(Q)uit\n"
# statement = input(ChoiceMenu).lower()
#
# while statement != QUIT_STATEMENT:
#     if statement == SMILE_STATEMENT:
#         print(":)")
#         total_smile += 1
#     elif statement == FROWN_STATEMENT:
#         print(":(")
#         total_frown += 1
#     else:
#         print("Invalid choice")
#     statement = input(ChoiceMenu).lower()
# print("Total Smile:",total_smile,"\nTotal Frown:",total_frown)
# =========================================================================
# ============= Total Numbers [ Algorithm ] ================
# #
# get numbers_to_add_up
# total = 0
# for i in range(numbers_to_add_up)
#     get number
#     total = total + number
# display total
# ============== Total Numbers [ Code ] ======================
# numbers_to_add_up = int(input("How many numbers do you want to add up? "))
# total = 0
# for i in range(1, numbers_to_add_up+1):
#     number = int(input(f"Enter number {i}: "))
#     total = total + number
# print("The total of those 3 numbers is",total)
# ============================================================
# ================= Guessing Game ============================
# ================= [ Algorithm ] ============================
# #
# total_guess = 0
# get guess
# while guess is not 6
#     if guess < 6
#         print("Higher")
#     else
#         print("Lower")
#     get guess
# display you got it in total_guess
# ============================================================
# =================== [ Code ] ================================
# SECRET = 6
# total_guess = 0
# guess = int(input("Guess a number: "))
# while guess != SECRET:
#     total_guess += 1
#     if guess < 6:
#         print("Higher")
#     else:
#         print("Lower")
#     guess = int(input("Guess a number: "))
# print(f"You got it in {total_guess} guesses!")
# =======================================================
# ================ Nested Loops ========================
# ================ [ Algorithm ] ========================
# #
# get rows
# get columns
# for row_number in range(rows)
#     for column_number in range(columns)
#         display column_number
#     go next line
# ================= [ Code ] ============================
# rows = int(input("Rows: "))
# columns = int(input("Columns: "))
# for row_number in range(rows):
#     for column_number in range(columns):
#         print(column_number, end=" ")
#     print()
# ==================================================
