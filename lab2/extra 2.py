'''If temperature is greater than 30,it's a hot day other wise if it's less than 10;
its a cold day;otherwise its a cold day. Else neither hot or cold'''

temp=float(input('enter temperature'))
if temp>30:
    print('it is a hot day')
elif temp<10:
    print('it is a cold day')
elif (temp>10) and (temp<30):
    print('it is neither hot nor cold')