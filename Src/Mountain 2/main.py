# Adrien (Leader/coder)/ Malo Jourdan-Brutti (coder)
# 23 February 2024

print("Welcome in the world")
print("For see your inventory, type i")
print("For start, type  s.")
user_input = input("Enter your answer: ")
user = user_input.lower()
if user_input == 's':
  print("You are in the world")
  print("You are in the forest")
  print("You can go to the mountain or the cave")
  print("You can take stick")
  print("Type st for take a stick")
  print("Type m if you want to go to the mountain or c if ou want to go to the cave")
  mountain = 'm'
  stick = 'st'
  cave = 'c'
  user_input = input("Enter your answer: ")  
elif user_input != 's':
  print("Goodbye")
  
while True:
  if user_input == 'm':
    print("You are in the mountain")
    print("You can go to the cave or the forest")
    print("Type c or f")
    cave = 'c'
    forest = 'f'
    user_input = input("Enter your answer: ")
  if user_input == 'c':
    print("You are in the cave")
    print("You can go to the mountain or the forest")
    print("Type m or f")
    mountain = 'm'
    forest = 'f'
    user_input = input("Enter your answer: ")
  if user_input == 'f':
    print("You are in the forest")
    print("There is a stick")
    print("Type st for have the stick")
    print("You can go to the cave or the mountain")
    print("Type c or m")
    cave = 'c'
    mountain = 'm'
    stick = 'st'
    user_input = input("Enter your answer: ")
    if user_input == 'st':
      print("You have a stick")
      print("The stick is in your inventory")
      print("Type i to see your inventory")
      mountain = 'm'
      stick = 'st'
      cave = 'c'
      user_input = input("Enter your answer: ")
  
     
   