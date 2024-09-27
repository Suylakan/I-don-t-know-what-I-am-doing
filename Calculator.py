import os
a = int(input("Please enter a number:")) #int command stops people from using letters. if you use letters it will only give you error and close
b = int(input("please enter another number:"))
c = input("please enter what to do? (+ means addition, - means substraction, / means division, * means multiplication): ")
if c == "+": #this code makes addition calculations
 print(a + b)
if c == "-": #this code makes substraction calculations
 print(a - b)
if c == "/": #this code makes division calculations
 print(a / b) 
if c == "*": #this code makes  multiplication calculations
 print(a * b)
else:
  print("Invalid Operation") #this part is for making sure people use "+", "-", "/" or "*" if people use something else it will show this error. I don't know why but this part keeps appearing after using right things :/
#this part is basic coding but if you are new to coding these codes does the calculations

os.system("pause")
#this code stops cmd from closing until you press a key
