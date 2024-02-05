'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Hav0
'''

random = 'car'
print("Is Random == 'car' true? I predict True.")
print(random=='car')
print("\n Is Random == 'bus'? I predict False.")
print(random == 'bus')

'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''
lists = []
name1 = 'Sunil'
name2 = 'Prabin'
lists.append(name1)
lists.append(name2)
if name1 == name2:
    print("These two are the same name")
else:
    print("Not same name")

if name1 == 'sunil'.title():
    print("This is equal.")
else:
    print("Not equal")

print('Sunil' in lists)
print('Ram' in lists)

'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
'''

alien_color = 'Green'
if alien_color=="Green":
    print("You earned 5 points")

# Another Version that fails the program 
alien_clr = 'Red'
if alien_clr=="Green":
    print("You earned 5 points")
else:
    print("You lost 5 points.")

'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5
points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
'''
alien_color = 'Green'

if alien_color == 'Green':
    print('the player just earned 5 points for shooting the alien.')
else:
    print('the player just earned 10 points.')

alien_color = 'Red'
if alien_color == 'Green':
    print('the player just earned 5 points for shooting the alien.')
else:
    print('the player just earned 10 points.')


'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.'''

alien_color = 'Red'

if alien_color == 'Green':
    print("The player earned 5 points")
elif alien_color == 'Yellow':
    print("The player earned 10 points")
elif alien_color == 'Red':
    print("The player earned 15 points")

alien_color = 'Green'

if alien_color == 'Green':
    print("The player earned 5 points")
elif alien_color == 'Yellow':
    print("The player earned 10 points")
elif alien_color == 'Red':
    print("The player earned 15 points")

alien_color = 'Yellow'

if alien_color == 'Green':
    print("The player earned 5 points")
elif alien_color == 'Yellow':
    print("The player earned 10 points")
elif alien_color == 'Red':
    print("The player earned 15 points")