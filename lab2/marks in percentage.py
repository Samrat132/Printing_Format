#WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail

subject_1=int(input('Enter the marks of subject_1:'))
subject_2=int(input('Enter the marks of subject_2:'))
subject_3=int(input('Enter the marks of subject_3:'))
subject_4=int(input('Enter the marks of subject_4:'))

total_marks=(subject_1+subject_2+subject_3+subject_4)
percentage=(total_marks/400)*100

WAP = print(f"The total marks of four subject is {total_marks} , percentage is {percentage}% and grade is ")

if percentage>70:
   print('A ')

elif percentage>60:
    print('B ')

elif percentage>40:
    print('C')

else:
    print('D')

