
# All Together Now
# #
# get choice
# while choice != "q"
# get choice
# while choice != "i" and choice != "c"
#     display Invalid choice
#     get choice
# if choice == "i"
#     display instructions
# else
#     get amount
#     get price
#
#     total_price = amount * price
#     if amount > 5
#         total_price *= 1 + 0.1
#
#     display total_price
# display Farewell

#
# DISCOUNT_PERCENTAGE = 10
# MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit\nChoice: "
# INSTRUCTIONS = "Enter the number of products you want to buy and your chosen price.\nIf you buy 0-5 times, they're full price, over 5 times and each one is 10% off!"
#
# choice = input(MENU).lower()
#
# while choice != "q":
#     if choice == "i":
#         print(INSTRUCTIONS)
#     else:
#         amount = int(input("Amount: "))
#         price = float(input("Price: "))
#         total_price = amount * price
#
#         if amount > 5:
#             total_price *= 1 - DISCOUNT_PERCENTAGE / 100
#         print(f"{amount}x${price} products = ${total_price}")
#     choice = input(MENU).lower()
#
# print("Farewell")