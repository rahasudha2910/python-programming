x= int(input("enter the number:"))
y= int(input("enter the number:"))
for z in range(x,y+1):
         sum = 0
         temp=z
         while temp > 0:
             digit = temp % 10
             sum += digit ** 3
             temp //= 10
 
         if z==sum:
             print(z)

