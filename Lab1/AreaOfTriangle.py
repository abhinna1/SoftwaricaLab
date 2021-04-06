''' Write a program that reads the length of the base and the height of a right-angled triangle and points the area.
Every number is given on a seperate line. '''

base = int(input('enter base of the right angled triangle'))
height = int(input('enter height of the right angled triangle'))
area = int(0.5 * base * height)
print('The area of the triange is ', area)