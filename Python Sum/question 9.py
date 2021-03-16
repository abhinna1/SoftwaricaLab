'''Write a program to find sum of the first n positive integers.
sum = (n*(n+1))/2'''
list = []
numOfNumber=int(input('enter number of numbers'))
for i in range(numOfNumber):
    if i==0:
        n = int(input('enter number'))
        list.append(n)
    else:
        n = int(input('enter next number'))
        list.append(n)
for j in range(numOfNumber):
    sum = 0
    sum =(list[j]+sum)

print(sum)