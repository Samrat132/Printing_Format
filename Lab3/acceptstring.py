#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string(s):
    e={"Upper_Case":0 , "Lower_Case":0}
    for i in s:
        if i.isupper():
            e["Upper_Case"]+=1

        elif i.islower():
            e["Lower_Case"]+=1


        print("Original Sring: ",s)
        print("No.of Upper Case characters: ", e["Upper_Case"])
        print("No.of Lower Case characters: ", e["Lower_Case"])

print(string('I Live In Nepal'))