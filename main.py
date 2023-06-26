#2
# welcome user to canteen
# ask for name
# welcome the user by name
print("Kia Ora!,")
print("Welcome to our school canteen!")
Name = input("What is your name? ")
if Name.isalpha():
  welcome = "Kia Ora, {name} welcome to the Fraser High School canteen."
  print(welcome.format(name=Name))

while Name.isalpha() == False:
  print("Sorry we really need to know your name to help us process this order")
  Name = input ("What is your name? ")

# s2
# ask user if they want to see the menu, yes or no
# if no thank user for visiting

menuQuestion = "{name} , would you like to see our awesome menu?  Please enter Yes or No."
menuResponse = input (menuQuestion.format(name=Name))

while menuResponse != "Yes" and menuResponse != "No":
  print("Sorry {name} , we need a Yes or No answer to help us.")

if menuResponse == "No":
  print("Thank you {name} for visiting us at Fraser High School Canteen.".format(name=Name))

# show menu to user