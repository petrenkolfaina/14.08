students = [
    ("Alex", 84),
    ("Kate", 74),
    ("Alice", 90),
    ("Nikita", 74),
    ("Bob", 84)
]

mydict = {}
for name, grade in students:
    if grade not in mydict:
        mydict[grade] = [name]
    else:
        mydict[grade].append(name)
print(mydict)

