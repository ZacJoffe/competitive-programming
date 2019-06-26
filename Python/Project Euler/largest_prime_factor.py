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




largestFactor = 5000
num = 600851475143
"""
i = num // 100000

while True:
    if isPrime(i) and num / i == num // i:
        largestFactor = i
        break
    i = i - 1
    print(i)

"""

for i in range(1, num):
    if isPrime(i) and num / i == num // i:
        largestFactor = i
        print(largestFactor)

print(largestFactor)
