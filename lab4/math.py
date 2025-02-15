#1
import math
def degre(n):
    return n * (math.pi/180)

n = float(input("Degree: "))
radian = degre(n)
print(f"Radian: {radian:.6f}") 


#2
import math
def trapezoid(a, b, h):
    return ((a*b)/2)*h 
  
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print("Area:", trapezoid(a, b, h))

#3
import math

def regular_pol(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

n = int(input("number of sides: "))
s = float(input("length of a side: "))

area = regular_pol(n, s)

print(f"The area of polygon: {area:.2f}")


#4
def parallelogram(a, h):
    return a * h
h = int(input("Height: "))
a = int(input("Length: "))
print("Area: ", parallelorgam(a, h))
