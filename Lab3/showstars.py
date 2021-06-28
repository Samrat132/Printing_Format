#Write a function called show_stars(rows).
# If rows is 5, it should print the following:***************

def show_stars(rows):

 for i in range(0, rows):
     print("\r")

     for j in range(0,i+1):
          print("*", end="")
show_stars(5)