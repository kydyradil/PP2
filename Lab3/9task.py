import math
radius=float(input(" "))

def sphere_volume(radius):
    return (4/3) *math.pi * radius ** 3

print("V=",sphere_volume(radius))