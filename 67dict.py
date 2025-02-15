from operator import index


country_capital = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "China": "Beijing",
}

cc = country_capital.copy()

print(cc)

# country_capital.pop("China")
# country_capital["Nepal"] = "Kathmandu"
# print(country_capital.values())

# Display by index



# print(country_capital)
country_capital["Japan"] = "Tokyo"
country_capital["Russia"] = "Moscow"

print(country_capital)

country_capital.update({"USA": "Washington DC"})
print(country_capital)

# del country_capital["India"] # to delete the key and value
# print(country_capital)

# display by index
print(country_capital["Nepal"])

print(country_capital.get("India"))
print(country_capital.keys())
print(country_capital.values())