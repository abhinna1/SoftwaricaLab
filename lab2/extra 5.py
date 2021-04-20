'''game finding a secret nuber within 3 attempts using wile loop'''

num=4
counter=1
while counter<=3:
    guess_Num=int(input('guess the number'))
    counter=counter+1
    if guess_Num==num:
        print('congratulations, you guessed the number')
        break
    elif counter==4:

        print('you failed')

    else:
        print('try again')
