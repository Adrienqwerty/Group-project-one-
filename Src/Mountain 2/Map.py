filename:Map.py

class Map:
  last_user_input = ''
  def __init__(self, name, description, items, exits):
      self.name = name
      self.description = description # Utilize the description argument
      self.user_input = 'mp'
  def access_map(self, user_input):
      def show_map():
          print("Map: Mountain is in north, Forest is in the middle of the map, and the cave is east ")
          if self.last_user_input == 'm':
              print("Mountain: You are on the Mountain")
          if self.last_user_input == 'f':
              print("Forest: You are in the Forest")
          if self.last_user_input == 'c':
              print("Cave: You are in the Cave")
      if user_input == 'mp':
          show_map()
  def some_function(self):
      print("Some function in Map module")