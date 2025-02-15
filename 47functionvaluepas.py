def mul(num):
    print(f"The multiplication table of {num} is: ")
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
    print("\n")

for i in range(1,101):
    mul(i)