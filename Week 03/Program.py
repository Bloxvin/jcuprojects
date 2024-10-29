# age = int(input("Age: "))
# mistakes = int(input("Mistakes: "))
#
# if mistakes >= age & age > 18:
# 	print("Welcome :)")
# else:
# 	print("Denied :(")
#
# age = int(input("Age: "))
# choice = input("Choose one of these \n\ta) multiply age by 2\n\tb) add 10 to age\n\tc) halve age\n\nChoice: ")
#
# if choice == "a":
# 	print(age*2)
# elif choice == "b":
# 	print(age+10)
# elif choice == "c":
# 	print(age/2)
# else:
# 	print("NO")
from cmath import phase
from idlelib.configdialog import changes
from lib2to3.fixer_base import BaseFix

# get ph
# if ph > 7.6
# 	Add Acid
# else if ph < 7.4
# 	Add Base
# else
# 	No Change

ph = float(input("PH: "))
if ph > 7.6:
	print("Add Acid")
elif ph < 7.4:
	print("Add Base")
else:
	print("No Change")









