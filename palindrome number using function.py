def palindrome():
    n=int(input("enter the number"))
    temp=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if(sum==temp):
        print(temp," is a palindrome number")
    else:
        print(temp,"is not a palindrome number")
palindrome()
