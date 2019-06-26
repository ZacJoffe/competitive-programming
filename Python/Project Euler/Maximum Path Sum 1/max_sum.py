file = open("path.txt")

path = []

for line in file:
    path.append(line)

print(maxSum(path))

def maxSum(path):
