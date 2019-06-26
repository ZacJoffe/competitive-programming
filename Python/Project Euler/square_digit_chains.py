def endIn(num):
    while num != 1 and num != 89:
        numStr = str(num)
        num = 0
        for i in range(0, len(numStr)):
            num += int(numStr[i]) ** 2
    
    return num 


count = 0

for i in range(1, 10000000):
    #print(i)
    if endIn(i) == 89:
        count = count + 1

print(count)