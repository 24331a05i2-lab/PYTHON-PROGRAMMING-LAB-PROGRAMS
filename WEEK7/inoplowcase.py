s=input("Enter a string: ")
ch=input("Enter a character: ")
if ch in s:
    print(ch," is present")
else:
    print(ch,"is not present")
    count=0
    for ch in s:
        if ch.islower():
            count=count+1
            print("Number of lowercase characters: ",count)