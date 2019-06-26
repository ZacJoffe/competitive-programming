def isMultiple(num):
    if num / 3 == num // 3 or num / 5 == num // 5:
        return True
    return False


sum = 0

for i in range(3, 1000):
    if isMultiple(i):
        sum += i

print(sum)
