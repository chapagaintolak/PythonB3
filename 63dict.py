country_capital = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "China": "Beijing",
}

print(country_capital["India"])

print(type(country_capital))

# Print Only Keys
print(list(country_capital.keys()))
print(list(country_capital.values()))

for k, v in country_capital.items():
    print(f"The capital of {k} is {v}")
