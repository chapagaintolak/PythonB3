scores = [65, 85, 90, 78, 88, 92, 56, 90]

scoremorethan70 = [x for x in scores if x > 70]
scorelessorequal = [x for x in scores if x <= 70]

total = len(scoremorethan70)
totalless = len(scorelessorequal)

print(f"Total student who scored more than 70: {total}")
print(f"Total student who scored less than or equal to 70: {totalless}")