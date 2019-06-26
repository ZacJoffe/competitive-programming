def digitalSum(num):
    sum = 0
    numStr = str(num)
    for i in range(0, len(numStr)):
        sum += int(numStr[i])
    return sum 

maxSum = 0

for a in range(0, 101):
    for b in range(0, 101):
        sum = digitalSum(a ** b)
        if sum > maxSum:
            maxSum = sum

print(maxSum)