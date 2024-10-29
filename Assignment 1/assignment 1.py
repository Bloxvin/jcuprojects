# CP1401 2024 TR3 Assignment 1
# Program 1 - Pizza Pay Calculator
# Student Name: Kaung Myat Kyaw
# Date started: 15/10/2024
#
# Pseudocode:
#
# display header
# get number_of_trips
# get number_of_minutes
# trips_pay = number_of_trips * 1.45
# minutes_pay = number_of_minutes * 0.95
# total_pay = trips_pay + minutes_pay
#
# display trips_pay
# display minutes_pay
# display total_pay
# ======================================
# Program 1 - Pizza Pay Calculator
# Code:
#
# PAY_PER_TRIP = 1.45
# PAY_PER_MINUTE = 0.95
#
# print("Warm Pizza Pay Calculator")
# number_of_trips = int(input("  Number of trips: "))
# number_of_minutes = int(input("Number of minutes: "))
# trips_pay = number_of_trips * PAY_PER_TRIP
# minutes_pay = number_of_minutes * PAY_PER_MINUTE
# total_pay = trips_pay+minutes_pay
#
# print(f"For {number_of_trips} trips, your pay is: ${format(trips_pay, ",.2f")}")
# print(f"For {number_of_minutes} minutes, your pay is: ${format(minutes_pay, ",.2f")}")
# print(f"Your total pay is ${format(total_pay, ',.2f')}")


# =============================================
# Program 2 - Tennis Results
# Pseudocode:
# #
# display welcome
# get your_score
# get opponent_score
# total_score = your_score + opponent_score
# if your_score > opponent_score
#     display you won
# elif your_score < opponent_score
#     display you lost
# else
#     display draw
#
# if total_score >= 8
#     display congratulations
# ===========================================
# Program 2 - Tennis Results
# Code:
#
# print("Welcome Player 1. How was your match?")
# your_score = int(input("\tYour score: "))
# opponent_score = int(input("Opponent score: "))
# total_score = your_score + opponent_score
#
# if your_score > opponent_score:
#     print("You won! :)")
# elif your_score < opponent_score:
#     print("You lost :( Keep trying.")
# else:
#     print("It's a draw.")
#
# if total_score >= 8:
#     print("Congratulations on playing a fast match!")
# ================================================
# Program 3 - Hiking Tracker
# Pseudocode:
#
# total_distance = 0
# display hiking tracker
#
# get number_of_days
# while number_of_days < 1
#     display Invalid number of days
#     get number_of_days
#
# for day in range(1, number_of_days+1)
#     get distance
#         while distance < 0 or distance > 120
#         display Invalid distance
#         get distance
#     total_distance += distance
#
# average_distance = total_distance/number_of_days
#
# display total_distance
# display average_distance
#
# if distance > average_distance
#     display above average
# elif distance < average_distance
#     display below average
# else
#     display the same
#
# ===============================================
# Program 3 - Hiking Tracker
# Code:
#
# total_distance = 0
# MIN_DISTANCE = 0
# MAX_DISTANCE = 120
# MIN_DAY = 1
# DISTANCE_UNIT = "km"
#
# print("Hiking Tracker")
# number_of_days = int(input("Number of days: "))
#
# while number_of_days < MIN_DAY:
#     print("Invalid number of days")
#
# for day in range(1, number_of_days+1):
#     distance = float(input(f"Day {day} distance: "))
#     while distance < MIN_DISTANCE or distance > MAX_DISTANCE:
#         print("Invalid distance")
#         distance = float(input(f"Day {day} distance: "))
#     total_distance += distance
#
# average_distance = total_distance / number_of_days
# print(f"Your total distance was   {total_distance}{DISTANCE_UNIT}")
# print(f"Your average distance was {average_distance}{DISTANCE_UNIT}")
#
# if distance > average_distance:
#     print("On your final day, your distance was above average.")
# elif distance < average_distance:
#     print("On your final day, your distance was below average.")
# else:
#     print("On your final day, your distance was the same as your average.")