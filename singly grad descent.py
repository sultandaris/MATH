from math import cos, sin

x = 2.5
for i in range(400):
    turunan = ((1+pow(x,2))*cos(x) - 2*x*(sin(x)))/ (pow(1+pow(x,2),2))
    xbaru = x - 0.01*turunan
    x = xbaru
    print("x:", x, "t:", turunan, "xb", xbaru)