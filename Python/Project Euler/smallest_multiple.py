def isDivisible(num):
    for i in range(2, 21):
        if num / i != num // i:
            return False
    return True

count = 2520

while isDivisible(count) == False:
    count = count + 10

print(count)
