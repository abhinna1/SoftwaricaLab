'''Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise they need to put
down 20%. Print the down payment'''
price=1000000
credit_Type=input('enter if good credit is True or False ')
if credit_Type=='True':
    down=int((price/100)*10)
elif credit_Type=='False':
    down=int((price/100)*20)
else:
    print('Enter correct credit type')
print(f'You down payment is ${down}%')