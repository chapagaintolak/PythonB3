n1 = 100
n2 = 101
n3 = 650

if n1> n2 and n1 > n3:
    print(f"{n1} is great than {n2} and {n3}")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is great than {n1} and {n3}")
elif n3 > n1 and n3 > n2:
    print(f"{n3} is great than {n1} and {n2}")
else:
    print("Something went wrong")

# and
# True and True is True
# True and False is False
# False and True is False
# False and False is False

# or
# True or True is True
# True or False is True
# False or True is True
# False or False is False