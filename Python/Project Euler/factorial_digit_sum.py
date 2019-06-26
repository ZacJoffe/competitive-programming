def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

num = str(fact(100))

sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
