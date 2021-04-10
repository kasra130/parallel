import math
print("Given a, and b")
a = float(input("enter a:\n"))
b = float(input("enter b:\n"))
decision = input("enter deg or rad :")

if (decision=="rad"):
    theta = float(input("enter the angle: \n"))
    c = float(math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(theta))))
    print(c)
else :
    thetadeg = float(input("enter the angle: \n"))
    degtorad = (thetadeg*(math.pi))/180
    d = float(math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(degtorad))))
    print(d)



