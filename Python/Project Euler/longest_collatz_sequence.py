def isEven(num):
    if num % 2 == 0:
        return True
    return False

def collatz(num):
    count = 1
    while num != 1:
        if isEven(num):
            num = num / 2
        else:
            num = 3 * num + 1

        #print(num)
        count = count + 1

    return count

highestCount = 0
highestNum = 0

for i in range(100, 1000000):
    if collatz(i) > highestCount:
        highestCount = collatz(i)
        highestNum = i

print(highestNum)
