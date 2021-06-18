'''
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
  else convert it to kg.
'''

weight = float(input('Enter your weight :'))
key = input("In which kg or lb you have typed.\n  'kg' for kilogram and 'lb' for poung:  ").lower()
forKg = "kg"
forLb = "lb"
print()

if key== forKg:
    inLb = weight * 2.20
    print(f"Your weight in pound is {inLb} lb")
elif key==forLb:
    inKg = weight/2.20
    print(f"Your weight in kilogram is {inKg} kg")
else:
    print("Invalid type !")
