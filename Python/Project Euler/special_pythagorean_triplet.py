import math

x = 0
y = 0
z = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a ** 2 + b ** 2)
        if c.is_integer() and (a + b + c) == 1000:
            x = a
            y = b
            z = c

print(x * y * z)
