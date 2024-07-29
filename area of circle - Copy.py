def circle(r):
    return r*r*3.14
r=int(input("enter the radius of circle:"))
print("area of circle=",circle(r))
def rectangle(l,b):
    return l*b
l=int(input("enter the length:"))
b=int(input("enter the breath :"))
print("area of ractangle=",rectangle(l,b))
def square(s):
    return s*s
s=int(input("enter the side value"))
print("area of square=",square(s))
def triangle(l,b,h):
    return l*b*h
l=int(input("enter the length="))
b=int(input("enter the breath="))
h=int(input("enter the height="))
print("area of triangle=",triangle(l,b,h))
