# intro to python data structures
# data structures are used for organizing information
# lists: can contain multiple data types, dynamic resizing
my_list = [1, "hello world", True]
print(my_list[-1])
print(*my_list, sep=', ')
my_list.append("hello")
print(*my_list, sep=', ')
print(my_list.pop())
print(my_list.pop(-1))
print(*my_list, sep=', ')
print(my_list)

# tuples: can contain multiple data types, immutable (size cannot be changed)
my_tuple = (1, "hello world", True)
print(my_tuple[0])
# my_tuple.append("hello")
# my_tuple[0] = 0

# dictionaries: key-value pairs, dynamic resizing
my_dict = {"name": "charlotte", "fav_color": "red", "fav_number": 24}
print(my_dict.get("name"))
# built-in print function for dictionaries!
print(my_dict)

dictionary = {"fav_num": 1, "greeting": "hello world", "is_raining": True}

my_dict["fav_color"] = "purple"
my_dict.pop("fav_number")
print(my_dict)


# OOP (object-oriented programming)
# this is a class blueprint for an object, in this case a person
class Person:
  # this is the class's constructor
  # I can set a default for the name and age parameters by doing name="Unknown" and age=0
  def __init__(self, n, a, c="default"):
    # these are the class's attributes
    self.name = n
    self.age = a
    self.fav_color = c

  # these are the class's methods
  def greet(self, person):
    print(f"Hello {person.name}!")

  def introduce(self):
    print(f"My name is {self.name} and I am {self.age} years old.")

  def increment_age(self):
    self.age += 1


# these are objects of the Person class
person_1 = Person("Joe", 20)
person_2 = Person("Jane", 21)
person_3 = Person("John", 22)
person_4 = Person("Jill", 4)

person_1.greet(person_2)
person_2.greet(person_1)

print(person_4.age)

print(person_1.name)

print(person_1)
print(person_2)


# Challenge: create a player class and instance (object) to demonstrate functionality
##### DO NOT SCROLL DOWN #####
class Player:

  def __init__(self, name, level=1, hp=10, df=5):
    self.name = name
    self.level = level
    self.hp = hp
    self.df = df

  def level_up(self):
    self.level += 1
    self.hp += 5
    self.df += 2

  def print_stats(self):
    print(
        f"Player {self.name}: Level {self.level}, HP {self.hp}, Defense {self.df}"
    )


player_1 = Player("Adam")
print(player_1)
# how can we make this print statement more informative?

# try adding this function to your class:
'''
def __str__(self): 
    return f"Player {self.name}: Level {self.level}, HP {self.hp}, Defense {self.df}"
'''

# __str__is an example of a special method, and so is __init__
