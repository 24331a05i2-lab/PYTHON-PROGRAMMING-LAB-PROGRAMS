file = open("sample.txt", "w")
file.write("Python Programming\n")
file.write("File Handling Methods\n")
lines = ["read()\n", "readline()\n", "readlines()\n"]
file.writelines(lines)
file.close()

file = open("sample.txt", "r")
print("Using read():")
print(file.read())
file.close()

file = open("sample.txt", "r")
print("Using readline():")
print(file.readline())
file.close()

file = open("sample.txt", "r")
print("Using readlines():")
print(file.readlines())
file.close()
