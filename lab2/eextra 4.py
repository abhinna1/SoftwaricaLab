'''Input the weight of a person in either kg or lbs, If the person provides his.
her weight in kg then conver it into lbs else convert to kg'''

weight = int(input('enter weight'))
unit = input('enter unit of weight')
if unit=='kg':
    weight_inlb=weight*0.453592
    print(f'The weight is {weight_inlb}lb.')
elif unit=='lb':
    weight_inkg=weight*2.20462
    print(f'the weight is {weight_inkg} kg.')