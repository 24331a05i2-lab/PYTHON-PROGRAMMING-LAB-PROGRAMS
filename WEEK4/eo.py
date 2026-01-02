n = int(input("Enter range: "))

even = 0
odd = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i + 1

print("No. of evens:", even)
print("No. of odds:", odd)
