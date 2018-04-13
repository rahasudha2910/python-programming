a=0
b=1
list=[a,b]
length=input("enter the length of fibonacci series:")
if length==1:
	print a
elif length==2:
	print a,b
elif length>=3:
	i=2
	while i<length:
		a=list[len(list)-2]
		b=list[len(list)-1]
		c=a+b
		list.append(c)
		i+=1
	print list
