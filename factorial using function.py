def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter the n value:"))
print("factorial of {} is {}".format(n,fact(n)))
