def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def isCircularPrime(n): # bool
    num = str(n)
    if isPrime(int(num)):
        for i in range(0, len(num)):
            num = rotate(num)
            if (not isPrime(int(num))):
                return False
        return True

    return False

def rotate(num): # returns rotated number as a string
    firstChar = num[0]
    for i in range(1, len(num)):
        num[i - 1] = num[i]

    num[len(num) - 1] = firstChar
    return num

print(isCircularPrime(197))
