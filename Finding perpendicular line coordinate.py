
import math
x2 = 2
y2 = 4
x1 = -3
y1 = 2
dist = 6.46

x3 = (x1 + x2) / 2
y3 = (y1 + y2) / 2

a = y2 - y1
b = x2 - x1

norm = math.sqrt(a*a + b*b)
c = a / norm
d = b / norm

x4 = x3 + c * dist
y4 = y3 + d * dist
print(x4,y4)
print(x3,y3)
print(a,b)
print(norm)
print(c,d)

