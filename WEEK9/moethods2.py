file = open("position.txt", "w+")

file.write("Python File Handling Example")

file.seek(0)

print("File content:")
print(file.read())

print("Current position using tell():", file.tell())

file.seek(7)
print("Pointer moved to:", file.tell())

file.write("PROGRAM")

file.flush()

file.close()