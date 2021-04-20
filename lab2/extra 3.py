'''If name is less than3 characters long- name must be at least 3 characters
otherwise if it's more than 50 characters- name must be maximum of 49 characters otherwise name looks giifd'''

name=str(input('enter name'))
if len(name)<3:
    print('Name mist be at least 3 characters')
elif len(name)>50:
    print('name must be maximum of 49 characters')
else:
    print('name looks good')