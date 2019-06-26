def howManyDigits(num):
    count = 0
    while num != 0:
        num = num // 10
        count = count + 1

    return count

count = 3

fib0 = 1
fib1 = 2

while howManyDigits(fib1) < 1000:
    temp = fib1
    fib1 = fib1 + fib0
    fib0 = temp
    print(fib1)
    count = count + 1

print(count)
