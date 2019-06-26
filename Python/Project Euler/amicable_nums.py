def d(n):
    sum = 1
    for i in range(2, n):
        if n / i == n // i:
            sum += i
    return sum

def isAmicable(a):
    b = d(a)
    if a != b and d(b) == a:
        return True
    return False

sum = 0

for i in range(219, 10000):
    if isAmicable(i):
        print(i)
        sum += i

print(sum)
