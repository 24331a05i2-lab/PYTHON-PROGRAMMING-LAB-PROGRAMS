a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

minimum = a
maximum = a

if b < minimum:
    minimum = b
if c < minimum:
    minimum = c

if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print("Minimum:", minimum)
print("Maximum:", maximum)
