def multiplication():
    n=int(input("enter the number"))
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
multiplication() 

def string():
    n="17"
    result=float(n)
    print(result)
string()

def string():
    n="27"
    result=int(n)
    print(result)
string()

def convert():
    s=[1,2,3,4,5,6,7]
    result=tuple(s)
    print(result)
convert()

def sum():
    n=int(input("enter the value of n"))
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)
sum()

def lcm():
    n1=int(input("first num"))
    n2=int(input("second num"))
    for i in range (n1,n2+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    lcm=n1*n2/gcd
    print("lcm=",lcm)
    print("gcd=",gcd)
lcm()
