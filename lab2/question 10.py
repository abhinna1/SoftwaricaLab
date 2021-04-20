'''Write a python program to sum of three given integers . However, if two values are equal sum will be zero'''

num1=int(input('enter first number'))
num2=int(input('enter second number'))
num3=int(input('enter third number'))
if num1==(num2 or num3):
    output=0
elif num2==(num1 or num3):
    output=0
elif num3==(num1 or num2):
    output=0
else:
    output= num1+num2+num3
print(output)