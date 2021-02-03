
#   LINK: https://careerkarma.com/blog/python-optional-arguments/


def count_coffees(coffees, to_find="Espresso"):
    number_sold = coffees.count(to_find)
    print("{} {} coffees were sold.".format(number_sold, to_find))

coffees_sold = ["Espresso", "Espresso", "Latte", "Cappuccino", "Mocha", "Espresso", "Latte"]

count_coffees(coffees_sold, "Latte")
count_coffees(coffees_sold)
print()

amy = {
	  "Name": "Amy",
	  "Final Assessment": 74,
	  "Second Test": 72,
	  "First Test": 68
}

def show_grades(student, **grades):
    print("Student record for {}: ".format(student))
    for key, value in grades.items():
        print("{} earned a grade of {} in their {}.".format(student, value, key))

show_grades(amy["Name"])
show_grades(amy["Name"], SecondTest=amy["Second Test"])
show_grades(amy["Name"], FirstTest=amy["First Test"], SecondTest=amy["Second Test"])
print()

