def isEven(num):
    if num % 2 == 0:
        return True
    return False

fib0 = 1
fib1 = 2
sum = 0

while fib1 < 4000000:
    if isEven(fib1):
        sum += fib1
    temp = fib1
    fib1 = fib1 + fib0
    fib0 = temp

print(sum)
