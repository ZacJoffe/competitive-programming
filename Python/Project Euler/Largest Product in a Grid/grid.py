file = open("grid.txt", "r")

temp = []
for i in file:
    temp.append(i)

grid = []

for i in range(0, len(temp)):
    grid.append()
    for j in range(0, len(temp[i])):
        grid[i].append(int(temp[j:j + 2])
