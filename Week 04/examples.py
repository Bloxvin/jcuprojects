MINIMUM_MONTH = 0
MAXIMUM_MONTH = 12

birth_month = int(input("Enter your birth month ({}-{}): ".format(MINIMUM_MONTH, MAXIMUM_MONTH)))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()