a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=(b*b-4*a*c)
if d==0:
    print("real and real roots",d)
elif d>0:
    print("different real roots",d)
else:
    print("imaginary roots",d)
    
