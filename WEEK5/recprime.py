def isPrime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return isPrime(n, divisor + 1)

num = int(input("Enter a number to check: "))

if isPrime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
