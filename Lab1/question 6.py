'''Solve each of the following problems using python scripts. Make sure you use appropriate variable names
and comments, When there is a final answer have python print it to the screen.
A person;s body mass index (BMI) is defined as:
BMI - mass in kg / (height in m)^2 '''

bodyMass=float(input('enter your body mass in KG')) #takes in body mass of person
height = float(input('enter your height in meters')) #takes in height of person
BMI = bodyMass/(height**2) #using formula for body mass index
print('Your body mass index is ',BMI) #prints the body mass index of person
