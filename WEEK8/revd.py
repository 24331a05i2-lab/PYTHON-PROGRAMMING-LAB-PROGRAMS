student = {"name": "Suhana","age": 19,"branch": "CSE"}
value = input("Enter value to find its key: ")
for key, val in student.items():
    if str(val) == value:
        print("Key found:", key)
        break
else:
    print("Value not found")