#2
# welcome user to canteen
# ask for name
# welcome the user by name
print("Kia Ora!,")
print("Welcome to our school canteen!")
namesetup = True
while namesetup == True:
  global name
  name = input("What is your name? ")
  if name.isalpha():
    welcome = "Kia Ora, {} welcome to the Fraser High School canteen."
    print(welcome.format(name))
    namesetup = False
  elif name.isalpha() == False:
    name = input ("What is your name? ")
    print("Sorry we really need to know your name to help us process this order")

# s2
# ask user if they want to see the menu, yes or no
# if no thank user for visiting


menuResponse1 = True
foodRespons1e1 = True
yes = ["yes","Yes","y","Y"]
no = ["no","No","n","N"]
while menuResponse1 == True:
  print( f"{name} , would you like to see our awesome menu? Please enter Yes or No.")
  menuQuestion = input()
  if menuQuestion in yes:
    menuResponse1 = False
  elif menuQuestion in no:
    print(f"Thank you {name} for visiting us at Fraser High School Canteen.")
    exit()
  else:
    print("Sorry {} we need a Yes or No answer to help us.".format(name))

# s3
# taking the users order
lastthing = True
finalResponse = "AE"
while lastthing == True:
  menuList = input(f"The Pie is worth $4.50 and The Burger is worth $7.89, {name} what would you like to order, either a Pie or Burger?  (Use lowercase) ")
  foodResponse = (menuList.format(name))
  if foodResponse == "pie":
    meal="pie"
    foodRespons1e1 = False
    lastthing = False
  elif foodResponse == "burger":
    meal="burger"
    foodRespons1e1 = False
    lastthing = False
  else:
    print(f"Sorry {name} we need to know if you would like a 'Pie' or a 'Burger'?".format(name))
finalResponse = f"Thank you {name} for ordering the delicious {meal}. We will just get this ready for you."
print(finalResponse.format(name=name))
