coffee = input("Select Coffee Type [ White or Black ]: ").lower()
size = input("Select Size [ Small or Medium or Large ]: ").lower()
if size == "small":
    cost = 3
elif size == "medium":
    cost = 4
else:
    cost = 5
if coffee != "black":
    cost += 1
print(f"a {coffee} {size} coffee would cost {cost}.")
