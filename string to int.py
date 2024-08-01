s="57"
int(s)
print (s)

a=[1,2,3,4,5]
sum=(a[0]+a[1]+a[2]+a[3]+a[4])
average=sum/5
print (average)

b=[1,2,3,4,5,6,7,8,9,10]
sum=0
for n in b:
    if n%2==0:
        sum=sum+n
if sum>0:
    print(sum)
else:
    print("no even numbers found")

m=[1,2,2,3,4,5,6,6,8,9,2,4,7]
m_duplicate=list(set(m))
print(m_duplicate)

import math
n=int(input("enter a number"))
p=math.sqrt(n)
if p.is_integer():
    print(n," is  a perfect square")
else:
    print(n,"is not a perfect square")
  
