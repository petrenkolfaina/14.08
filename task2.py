students = {
    "Alex": 84,
    "Kate": 69,
    "Alice": 90,
    "Nikita": 74,
    "Bob": 45
}


def average(students):
    average_grade = sum(students.values())/len(students)
    return(average_grade)


print(average(students))
