from matplotlib.pylab import f

fruits = ['Apple', 'Orange', 'Mango']
# Make all list upper case
fruits = [r.upper() for r in fruits]

fruit_name = input("Enter a fruit name: ")

if fruit_name.upper() in fruits:
    print(f"{fruit_name} is available")
else:
    print(f"{fruit_name} is not available")