'''WAP to find the maximum of 3 numbers'''
num1=int(input('enter furst number'))
num2=int(input('enter second number'))
num3=int(input('enter third number'))

print(max(num1,num2,num3))

#OR

if num1>(num2 and num3):
    max=num1
elif num2>(num1 and num3):
    max=num2
elif num3>(num1 and num2):
    max=num3
print(max)