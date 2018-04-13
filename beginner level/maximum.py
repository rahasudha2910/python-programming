x= []
y= int(input('How many numbers: '))
for n in range(y):
    numbers = int(input('Enter number '))
    x.append(numbers)
print(max(x))
