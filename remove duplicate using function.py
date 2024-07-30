def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
def gcd():
    n1=int(input("first num"))
    n2=int(input("second num"))
    for i in range (n1,n2+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    print("gcd=",gcd)
gcd()
