# # Python Coding - Input, Processing and Output
#
# original_price = float(input("Original price: $"))
# surcharge_rate = float(input("Surcharge % (e.g 0.15 is 15%): "))
# extra_charge = original_price * surcharge_rate
# total_price = original_price + extra_charge
# print("The total meal price is $", total_price, sep="")
#
# ================================================
# # [1] Discount Price Coding Exercise
#
# DISCOUNT_RATE = 0.2
# original_price = float(input("Enter the original price: "))
# discount_price = original_price * DISCOUNT_RATE
# new_price = original_price - discount_price
#
# print("The price after discount is: ", new_price, ".")
#
# ================================================
# # [2] Kilometres to Miles Coding Exercise
#
# get kilometre
# mile = kilometre * 0.621371
# print mile
#
# KILOMETRE_TO_MILE_RATIO = 0.621371
# kilometre = float(input("Enter the distance in kilometre: "))
# mile = kilometre * KILOMETRE_TO_MILE_RATIO
# print("The distance in mile is: ", mile,".")
#
# ================================================
# # [3] Holiday Cost
#
# get daily_food_cost
# get daily_activities_cost
# get number_of_days
# trip_cost = (daily_food_cost+daily_activities_cost)*number_of_days
# print trip_cost
#
# daily_food_cost = float(input("Daily food cost: $"))
# daily_activities_cost = float(input("Daily activities cost: $"))
# number_of_days = int(input("Number of days: $"))
# trip_cost = (daily_food_cost+daily_activities_cost)*number_of_days
# print("\nThe trip will cost $",format(trip_cost, "0.1f"))
# ================================================
# # [4] Deep Sleep Calculation ( Percentage )
#
# total_sleep_in_seconds = int(input("Total sleep in seconds: "))
# deep_sleep_in_seconds = int(input("Deep sleep in seconds : "))
#
# deep_sleep_in_minutes = deep_sleep_in_seconds // 60
# deep_sleep_in_remaining_seconds = deep_sleep_in_seconds % 60
# total_sleep_in_minutes = total_sleep_in_seconds // 60
# total_sleep_in_remaining_seconds = total_sleep_in_seconds % 60
# percentage = deep_sleep_in_seconds/total_sleep_in_seconds * 100
# print("\nDeep sleep : ", deep_sleep_in_minutes,"m ", deep_sleep_in_remaining_seconds,"s", sep="")
# print("Total sleep: ", total_sleep_in_minutes,"m ", total_sleep_in_remaining_seconds,"s", sep="")
# print("Percentage : ",percentage,"%")
