''' Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are
 displayed  on the 24hr digital clock?
 The program should print two numbers: the number  of hours(between0 and 23) and the number of minutes(between 0 and 59).
 For example, if N = 150, then 150 minutes have passed since midnight -i.e now is 2:30 an, So, the program should print 2:30'''

N = int(input('enter number of minutes passed since midnight'))
hours =N//60
sminutes = N%60
print(hours, 'hours and', minutes, 'minutes have passed since midnight')
