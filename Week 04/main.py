# # START_RANGE = 60
# # END_RANGE = 131
# # INCREMENT = 10
# # CONVERSION_FACTOR = 0.6214
# #
# # print('KPH \t MPH')
# # for kph in range(START_RANGE, END_RANGE, INCREMENT):
# #     mph = kph * CONVERSION_FACTOR
# #     print(format(kph, ".1f"),"\t",format(mph, ".1f"))
# #
# # # display kph to mph table header
# # # for kph in range(60, 131, 10)
# # #     mph = kph * 0.6214
# # #     display kph mph
# #
# # get start_square_number
# # get end_square_number
# # display number to square header
# # for number in range(start_square_number, end_square_number)
# #     square_number = number**2
# #     display number and square number
# #
# # start_square_number = int(input("Start square number: "))
# # end_square_number = int(input("Final square number: "))
# # print("Number\tSquare Number\n===================")
# # for number in range(start_square_number, end_square_number+1):
# #     print(number,"\t",number**2)
#
# # get lot_no
# #
# # while lot_no != 0
# #     get lot_price
# #     tax = lot_price * 0.00675
# #     display lot number with tax
# #
# # display end
# #
# # TAX_RATE = 0.00675
# # lot_no = int(input("Lot Number ( 0 to end ): "))
# #
# # while lot_no != 0:
# #     lot_price = float(input("Lot Price: "))
# #     tax = lot_price * TAX_RATE
# #     print("Lot Number: ",lot_no,"| Tax: $",format(tax, ",.2f"), sep="")
# # print("Ended")
#
# for days in range(30):
#     for hours in range(24):
#         for minutes in range(60):
#             for seconds in range(60):
#                 print(f"Days: {days} | Hours: {hours} | Minutes: {minutes} | Seconds: {seconds}")
#                 input()
# 1.
for i in range(6):
    print(i, end=' ')
print()

# 2.
for i in range(33, 39):
    print(i, end=' ')
print()

# 3.
for i in range(17, 11, -1):
    print(i, end=' ')
print()

# 4.
for i in range(1, 11):
    print(i % 2, end=' ')
print()

# 5.
for i in range(7,-6,-3):
    print(i, end=" ")
print()
