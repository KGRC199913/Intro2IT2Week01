def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def lowPrimes(n):
    i = 0
    for i in range(n, 2):
        if isPrime(i):
            break
    return i


def highPrime(n):
    i = n
    while True:
        if isPrime(i):
            return i
        else:
            i += 1


x = int(input("nhap vao mot so:\n"))
if isPrime(x):
    print(x)
else:
    LowPrime = lowPrimes(x)
    HighPrime = highPrime(x)
    delta_low = x - LowPrime
    delta_high = HighPrime - x
    if delta_high >= delta_low:
        print(LowPrime)
    else:
        print(HighPrime)
