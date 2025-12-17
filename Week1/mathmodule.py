import math 
r=float(input("Enter radius of the Circle: ")) 
a= math.pi*r*r 
print("The Area of the circle: ", round(a,2)) 
s=float(input("\nEnter the Number whose Square root is to be evaluated: ")) 
sr=math.sqrt(s) 
print("The Square root the given number is: ",sr) 
angle=float(input("\nEnter angle in degree: ")) 
print("The sin of the given angle is: ",round(math.sin(math.radians(angle)),4)) 
print("The cos of the given angle is: ",round(math.cos(math.radians(angle)),4))
