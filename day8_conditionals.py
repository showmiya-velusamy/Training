name1=input("enter the name1: ")
height1=int(input("Enter the height1 :"))
name2=input("enter the name2: ")
height2=int(input("Enter the height2 :"))
if(height1>height2):
  print(name1 + " is taller than " + name2)
else:
  print(name2 + " is taller than " + name1)
# Task 1
stock1 = "vanilla"
stock2 = "lime"
stock3 = "chocolate"
# Ask user their fav flavour
favourite=input("Enter your favourite flavour: ")
if(favourite==stock1):
  print("Yes,we do have it")
elif(favourite==stock2):
  print("yes,we do have it")
elif(favourite==stock3):
  print("Yes,we do have it")
else:
  print("No,we don't have it")

#task 2
#code better
stock1 = "vanilla"
stock2 = "lime"
stock3 = "chocolate"
favourite=input("Enter your favourite flavour: ")
if favourite in (stock1,stock2,stock3):
  print("Yes,we do have it")
else:
  print("No,we do not have it")

#task 3
#using ternary operator
shop_stock="vanilla","lime","chocolate"
print("Yes,we do have it" 
if(favourite in shop_stock) 
else "No,we do not have it")