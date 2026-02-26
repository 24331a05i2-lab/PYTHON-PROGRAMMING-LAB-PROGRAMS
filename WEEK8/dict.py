student = { "name": "Suhana", "age": 19,"branch": "CSE"}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
removed = student.pop("age")
print("After pop():", student)
del student["branch"]
print("After delete:", student)