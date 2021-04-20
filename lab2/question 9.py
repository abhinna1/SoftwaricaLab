year=int(input('enter year'))

if (year%4==0) or (year%400==0):
    year_type='Leap Year'
elif year%400==0:
    year_type='Leap Year'
else:
    year_type='Common Year'
print(year_type)