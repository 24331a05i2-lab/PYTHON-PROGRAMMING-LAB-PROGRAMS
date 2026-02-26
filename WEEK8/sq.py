n = int(input("Enter the value of n: "))
result = []
for i in range(1, n+1):
    result.append((i, i*i))
print("List of tuples:", result)