import math

def howManyDisors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):

            # If divisors are equal,
            # count only one
            if (n / i == i):
                cnt = cnt + 1
            else: # Otherwise count both
                cnt = cnt + 2

    return cnt

i = 1
j = 1

while howManyDisors(j) <= 500:
    i = i + 1
    j = j + i

print(j)
