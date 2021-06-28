#Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# Accept string from the user and display only those characters which are present at an even index.

string=input('Enter the string: ')

def palindrome(string):
   temp=string
   rev=string[::-1]

   if temp == rev:
      print('It is a palindrome')

   else:
      print('It is not a palindrome')

palindrome(string)