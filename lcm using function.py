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

def convert():
    n=(2,5,7,9,)
    result=list(n)
    print(result)
convert()
