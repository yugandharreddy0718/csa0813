def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter the n value:"))
print(fact(n))

m=int(input("enter a year"))
if m%4==0:
    print(m," is leap year")
elif m%400==0:
    print(m," leap year")
else:
    print(m,"not a leap year")
