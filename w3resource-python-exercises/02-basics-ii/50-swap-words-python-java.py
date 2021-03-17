input_text = "Python is popular than Java"
print(input_text)

input_text = input_text.replace("Python", "XXXX")
input_text = input_text.replace("Java", "Python")
input_text = input_text.replace("XXXX", "Java")

print(input_text)
