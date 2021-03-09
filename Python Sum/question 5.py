
'''
A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased
The program should read three integers: the number of students in each of the three classes, a, v and c respectively.
In the first test there are three groups. The first group has students and thus needs 10 desks,
The second group has 21 students. so that can get by with no fewer than 11 desks in total
'''

studentsIn_Class1= int(input('enter number of students'))
studentsIn_Class2= int(input('enter number of students in class 2'))
studentsIn_Class3= int(input('enter numbbber of students in class 3'))
totalStudents= studentsIn_Class1+studentsIn_Class2+studentsIn_Class3
numberOfBenches = totalStudents/2
number = round(numberOfBenches)
print(number,' benches are required in the class')

