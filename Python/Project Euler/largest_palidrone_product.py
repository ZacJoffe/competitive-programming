def isPalindrome(num):
    numStr = str(num)
    backwards = ''
    i = len(numStr) - 1
    while i >= 0:
        backwards = backwards + numStr[i]
        i = i - 1
    # print (numStr, " ", backwards)

    if numStr == backwards:
        return True
    return False

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i * j) and i * j > largest:
            largest = i * j

print(largest)
