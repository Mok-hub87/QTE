import math
def triangle(x,y,z):
    p=(x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s
def squear(x,y):
    s=x*y
    return s
def circle(x):
    s=math.pi*(x**2)
    return s
f=(input("фигура:"))
if f=="треугольник":
    x = int(input())
    y = int(input())
    z = int(input())
    print("площадь треугольника",triangle(x,y,z))
elif f=="приямоуголник":
    x=int(input())
    y=int(input())
    print("площадь прямоугольника",squear(x,y))
elif f=="круг":
    x=int(input())
    print("площадь круга",circle(x))
