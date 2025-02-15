marks = {
    "som": 90,
    "binaya":  80,
    "soma": 70,
    "bina": 60
}

studentnamewith_80_plus = []

for k, v in marks.items():
    if v >=80:
        studentnamewith_80_plus.append(k)

print(studentnamewith_80_plus)