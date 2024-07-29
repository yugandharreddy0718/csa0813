n=int(input("enter a year"))
if n%4==0:
    print(n," is a leap year")
elif n%400==0:
    print(n," is a leap year")
else:
    print(n," is not a leap year")
    
