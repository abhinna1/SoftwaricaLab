'''WAP called showNumbers that takes a parameter called limit. It should print
all the numbers between 0 and limit with a label to identify the even and off numbers.
For example if the limit is 3, it should print:
1) 0 EVEN
2) 1 ODD
3) 2 EVEN'''

def showNumbers(limit):
    odd_counter=0
    even_counter=0
    for i in range(0,limit+1):
        if i%2==0:
            even_counter+=1
        elif i%2!=0:
            odd_counter+=1
        return f'{odd_counter} ODD {even_counter} EVEN'

print(showNumbers(5))