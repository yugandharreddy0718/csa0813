import math
n=int(input("enter a number"))
p=math.sqrt(n)
if p.is_integer():
    print(n," is  a perfect square")
else:
    print(n,"is not a perfect square")
