# welcome user to canteen
# ask for name
# welcome the user by name
print("Hello!,")
print("Welcome to our canteen!")
Name = input("What is your name? ")
if Name.lower():
  welcome = "Hello and welcome {name}, Welcome to our canteen!"
print(welcome.format(name=Name))

while Name.lower() == False:
  print("Sorry we need your name for your order!")
  Name = input ("What is your name? ")