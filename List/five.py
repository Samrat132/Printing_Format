# Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def lst(string):
    word = 0

    for i in string:
        if len(i) > 1 and i[0] == i[-1]:
            word+=1
    return word

print(lst(['abc','xyx','aba','1221']))