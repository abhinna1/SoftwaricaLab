'''N students take K apples and distribute them among each other evenly.
The remaining (the undivisible) part remains in the basket. How many apples will each single student get?
 How many apples will remain in the basket? The program reads the number N and K.
 It should print the two answers for the questions above'''

N = int(input('enter number of students'))
K = int(input('enter number of apples'))

applePerStudent = K//N
remainingApples = K-(applePerStudent*N)
print('each student gets ',applePerStudent)
print('reamaing apples are ', remainingApples)