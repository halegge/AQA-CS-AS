def primeChecker(n):
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
    if isPrime:
        print(str(n) + " is a prime number")
    else:
        print(str(n) + " isn't a prime number")

primeChecker(12)
