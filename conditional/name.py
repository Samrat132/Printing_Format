'''
  If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
'''
name =len(input("Enter the name :"))

if (name<3):
    print('name must be at least 3 characters')
elif (name>50):
    print('name must be maximum of 50 characters')
else:
    print('name looks good!')