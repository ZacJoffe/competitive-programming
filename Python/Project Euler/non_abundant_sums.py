def isAbundant(num):
    sum = 0
    for i in range(1, num):
        if num / i == num // i:
            sum += i
    if sum > num:
        return True
    return False

sum = 0

for i in range(1, 28123):
    
