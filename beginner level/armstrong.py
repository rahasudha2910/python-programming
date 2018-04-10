x=int(input())
order=len(str(x))
sum=0
temp=x
while temp > 0:
   digit=temp%10
   sum+=digit**order
   temp//=10
if x==sum:
   print(x,"yes")
else:
   print(x,"no")
