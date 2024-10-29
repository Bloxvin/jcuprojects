# """choice = input("Steak choice (rare, medium, well-done or burnt): ").lower()
# if choice == "rare":
#     print("2 minutes")
# elif choice == "medium":
#     print("4 minutes")
# elif choice == "well-done":
#     print("6 minutes")
# elif choice == "burnt":
#     print("8 minutes")
# else:
#     print("Ain't no steak like that here")"""
#
###################################

# #1. Tax
# -------------------- Algorithm ----------------------
# get income
# if income < 100
#     total_tax = income * 0
# else if income < 500
#     total_tax = income * 0.02
# else if income < 1000
#     total_tax = income * 0.05
# else
#     total_tax = income * 0.1
# take_home_pay = income - total_tax
# #
# ------------------ Python Code -------------------------
# TAX_RATE_LOW = 0.02
# TAX_RATE_MID = 0.05
# TAX_RATE_HIGH = 0.1
# TAX_THRESHOLD_LOW = 100
# TAX_THRESHOLD_HIGH = 1000
# TAX_THRESHOLD_MID = 500
#
# print("Python Party Tax Program - Where Tax is a Party")
# income = float(input("Income: $"))
# if income < TAX_THRESHOLD_LOW:
#     total_tax = 0
# elif income < TAX_THRESHOLD_MID:
#     total_tax = income * TAX_RATE_LOW
# elif income < TAX_THRESHOLD_HIGH:
#     total_tax = income * TAX_RATE_MID
# else:
#     total_tax = income * TAX_RATE_HIGH
# take_home_pay = income - total_tax
#
# print("Total tax is: $", total_tax, sep="")
# print("Take home pay is: $", take_home_pay, sep="")
#
#####################################
# # 2. Car Insurance
# -------------- Algorithm ---------------- #
# get age
# if age < 18
#     refuse hire
# else if age < 25
#     required to purchase special insurance
# else
#     not required to purchase insurance
#
# ------------------- Python Code ---------------------
# REFUSAL_AGE = 18
# INSURANCE_NOT_REQUIRED_AGE = 25
# age = int(input("Age: "))
# if age < REFUSAL_AGE:
#     print("Hire refused")
# elif age < INSURANCE_NOT_REQUIRED_AGE:
#     print("Insurance required")
# else:
#     print("Insurance not required")
################################################
#
# 3. Simple Password Cracker
# ------------------ Algorithm --------------#
# SECRET_PASSWORD = "asdf"
# get passwordinput
# if passwordinput == SECRET_PASSWORD
#     display "Access granted"
# else
#     display "Access denied"
#
# ---------------- PYTHON CODE --------------------
# SECRET_PASSWORD = "asdf"
# passwordinput = input("Password: ")
# if passwordinput == SECRET_PASSWORD:
#     print("Access granted")
# else:
#     print("Access denied")
#############################################################
# 4. Basketball
#
# ----------------- Algorithm ---------------------------
# get attempted_shots
# get made_shots
# shooting_percentage = made_shots / attempted_shots * 100
#
# display attempted_shots
# display made_shots
# display shooting_percentage
# if shooting_percentage > 50
#     display "That's great!"
# --------------- Python Code --------------------------
# attempted_shots = int(input("Shots attempted: "))
# made_shots = int(input("Shots made: "))
# shooting_percentage = made_shots/attempted_shots*100
#
# print("Number of shots attempted:", attempted_shots)
# print("Number of shots made:",made_shots)
# print("Your shooting percentage is ",shooting_percentage,"%",sep="")
#
# if shooting_percentage > 50:
#     print("That's great!")
##################################################
# 5. Rock of Ages
#
# ------------------------ Algorithm -----------------
# #
# get age
# if age < 0 and age > 120
#     display "Invalid Age"
# else if age < 13
#     display "Child"
# else if age < 18
#     display "Teenage"
# else if age < 30
#     display "Young Adult"
# else if age < 60
#     display "Adult"
# else
#     display "Elderly"
# # -------------------------- Python Code -----------------
# MINIMUM_AGE = 0
# MAXIMUM_AGE = 120
# CHILD_AGE = 13
# TEEN_AGE = 18
# YOUNG_ADULT_AGE = 30
# ADULT_AGE = 60
#
# age = int(input("Age: "))
# if age < 0 and age > 120:
#     print("Invalid Age")
# elif age < 13:
#     print("Child")
# elif age < 18:
#     print("Teenage")
# elif age < 30:
#     print("Young adult")
# elif age < 60:
#     print("Adult")
# else:
#     print("Elderly")
###################################################
# 6. Speeding Fines
#
# --------------------------- Algorithm ----------------------------
# get speed
# get speed_limit
# over_speed_limit = speed - speed_limit
#
# if over_speed_limit < 0
#     display "Not Over Speed Limit"
# else if over_speed_limit < 11
#     display "$309 Penalty"
# else if over_speed_limit < 20
#     display "$464 Penalty"
# else if over_speed_limit < 30
#     display "$696 Penalty"
# else if over_speed_limit < 40
#     display "$1161 Penalty"
# else
#     display "$1780 Penalty"
# --------------------- Python Code -------------------------
#
# FIRST_LIMIT = 11
# SECOND_LIMIT = 20
# THIRD_LIMIT = 30
# FOURTH_LIMIT = 40
# speed = float(input("Speed: "))
# speed_limit = float(input("Speed Limit: "))
# over_speed_limit = speed - speed_limit
#
# if over_speed_limit < 0:
#     print("Not over speed limit")
# elif over_speed_limit < FIRST_LIMIT:
#     print("$309 Penalty")
# elif over_speed_limit < SECOND_LIMIT:
#     print("$464 Penalty")
# elif over_speed_limit < THIRD_LIMIT:
#     print("$696 Penalty")
# elif over_speed_limit < FOURTH_LIMIT:
#     print("$1161 Penalty")
# else:
#     print("$1780 Penalty")



