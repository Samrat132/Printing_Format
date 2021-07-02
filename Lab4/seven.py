#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

lst=[0,1,2,3,4,5,6]
lst.remove(3)
lst.remove(6)
print(lst)

for i in range(6):
    if (i ==3 or i ==6):
        continue
    print(i,end="")
