''' WAP which accepts marks of four subjects and display total marks, percentage annd grade
Hint: more than 70% --> disctinction, more than 60%--> first, more than 40%-->pass,less than 40%--> fail'''

subject1=int(input('marks in first subject'))
subject2=int(input('marks in second subject'))
subject3=int(input('enter marks in third subject'))
subject4=int(input('enter marks in fourth subject'))

percentage = (subject1+subject2+subject3+subject4)/400
if (percentage>=70)and(percentage<100):
    print("distinction")
elif (percentage<=69)and(percentage>=60):
    print('first division')
elif(percentage<=)