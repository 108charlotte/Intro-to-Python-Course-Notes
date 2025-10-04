print("Examples and for Loops")
# for loop example (make a staircase)
'''
outcome: 
#
##
###
'''
for i in range(3): 
  print("#"*(i+1))

# what is happening here? 
# when you multiply a string by a number, the string will repeat however many times the number is
# so why doesn't this cause a data type mismatch error? 
# this is because python knows that when it sees a string and then a number, it should repeat the string that many times

# this will also work in the reverse (try it out yourself)! 
print(18*"hi ")

# just a quick note, you can also do some other cool things with the print function, such as automatically adding a space between words: 
print("hello", "world")

# or setting what you have between the words to something else: 
print("hello", "world", sep=", ")

# for loop challenge (flip the staircase)
'''
outcome: 
  #
 ##
###
'''
for i in range(3): 
  # note that I am taking advantage of python following order of operations here
  # 2 is the largest number in the range, so the space will be printed 2-i times, or 2, 1, 0 times
  print(" "*(3-i),end="")
  print("#"*(i+1))

# for loop challenge (2 #s per stair)
'''
outcome: 
    ##
  ####
######
'''
for i in range(3): 
  print("  "*(2-i),end="")
  print("##"*(i+1))

print("\nFunctions Practice")
# what if we could write a function that would print these staircases?
def function_name(par1, par2): 
  print(par1 + par2)

num = function_name(1, 2)
print(num)

# challenge: write a function that takes the number of rows and prints the staircase
print("\n1st Function Challenge")
def print_staircase(rows): 
  for i in range(rows): 
    print(" "*(rows-i-1),end="")
    print("#"*(i+1))

# test your function to print the 3-row staircase from before, then with a few other heights to see if it still works! 
print_staircase(3)
print_staircase(5)

print("\n2nd Function Challenge")
# challenge: update your function to also take the number of #s per stair
def print_custom_staircase(rows, blocks_per_stair): 
  for i in range(rows): 
    print(" "*(rows-i-1)*blocks_per_stair,end="")
    print("#"*(i+1)*blocks_per_stair)

# now test it! 
print_custom_staircase(3, 2)
print_custom_staircase(5, 3)

print("\n3rd Function Challenge")
# challenge: update your function to also take the character to print (instead of #)
def print_custom_staircase_with_character(rows, blocks_per_stair, char): 
  for i in range(rows): 
    print(" "*(rows-i-1)*blocks_per_stair,end="")
    print(char*(i+1)*blocks_per_stair)

print_custom_staircase_with_character(3, 2, "*")

print("\nWhile Loops")
# a while loop is a type of loop that runs as long as its condition is true

raining = True
while raining: 
  raining = False

# challenge: write a while loop that counts down from 10 to 1, then prints "Takeoff!"
n = 10
while n > 0: 
  print(str(n) + "...")
  # this is an abbreviated version of n = n - 1, which is how you update a variable in python
  # n -= 1 is shorthand, since programmers update variables a lot
  # what would happen if I commented out this line? why? 
  n -= 1
print("Takeoff!")

def return_10(): 
  print("This will never run")
  return 10

# what will this loop do? (don't run it yet!)
while True: 
  if input("Enter something: ") == "hello": 
    break

# since True is always true, this loop will run forever! Now that you have seen this, make a guess as to what the below loop will do

'''
while 1 == 1: 
  input("Enter something: ")
'''

# why do these loops exist? well, you are actually able to stop them, making them much more useful, particularly in games and for recieving user input
