import random
file = open("sample.txt", "w")
print("Random Numbers:")
for i in range(20):
    num = random.randint(1, 100)
    print(num)
    file.write(str(num) + "\n")
file.close()