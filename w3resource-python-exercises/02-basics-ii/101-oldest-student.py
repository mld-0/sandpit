
def oldest_student(students):
    """Print oldest student in dictionary"""
    students_sorted = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
    oldest_student = list(students_sorted.keys())[0]
    print(oldest_student)


oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15})
oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7})
