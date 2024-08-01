s="57"
int(s)
print(s)


a=eval(input("enter the list="))
sum=0
length=len(a)
for i in a:
    sum=sum+i
average=sum/length
print("average list of integers=",average)



b=[1,2,3,4,5,6,7,8,9,10]
sum=0
for n in b:
    if n%2==0:
        sum=sum+n
if sum>0:
    print(sum)
else:
    print("no even numbers found")


import math
n=int(input("enter a number"))
p=math.sqrt(n)
if p.is_integer():
    print(n," is  a perfect square")
else:
    print(n,"is not a perfect square")

    
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6]
c= list(set(b))

print(c)
