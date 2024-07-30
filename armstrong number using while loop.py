n=int(input("Enter a number: "))
temp=n
sum=0
while n>0:
    m=n%10
    sum=sum+m*m*m
    n=n//10
if temp==sum:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")
