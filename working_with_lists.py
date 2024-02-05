# """4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should
# have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!"""

# pizzas = ['Margherita', 'Chicken Pizza', 'Cheese Pizza']
# for pizza in pizzas:
#     print(f"I like {pizza}.")
# print("how much do you like pizza ?")
# print("I really love pizza")


# '''
# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A
# dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in
# common. You could print a sentence, such as Any of these animals would make a great pet!
# '''
# animals = ['Dog', 'Goat', 'Cow', 'Buffalo']

# for animal in animals:
#     print(animal)
# print("\nStatements about each animal:")

# for animal in animals:
#     print(f"A {animal.lower()} would make a great pet.")

# print("\nCommon characteristic:")
# print("Any of these animals would make a great pet!")


# '''
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list.
# '''
# lists = ['Sushma', 'Soniya', 'Supriya']
# print(lists[0])
# print(lists[1])
# print(lists[2])
# middle_start = len(lists)//2-1
# middle_end  = middle_start+3
# print(middle_end)
# print(middle_start)

# print(lists[middle_start:middle_end])

# print(lists[0:3])

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
'''

fav_pizzas = ['Margherita', 'Chicken Pizza', 'Cheese Pizza']
friend_pizzas = ['Margherita', 'Chicken Pizza', 'Cheese Pizza']
friend_pizzas.append("Mushroom Pizza")

print("My favourite pizza are: \n")
for pizza in fav_pizzas:
    print(pizza)

print("\n")


print("My friend's favourite pizza are: \n")
for fpizza in friend_pizzas:
    print(fpizza)


"""4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods."""

foods_version = [
    ["Pizza", "Burger", "Pasta"],
    ["Apple", "Banana", "Orange"],
    ["Chicken", "Fish", "Beef"]
]
foods  =[]

for food_items in foods_version:
    print(food_items)

for food_items in foods_version:
    for food in food_items:
        foods.append(food)
print(foods)
