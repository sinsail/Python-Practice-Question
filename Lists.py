# '''3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.'''

# lists = ['Sushil', 'Sunil', 'Srijan', 'Prashant','']
# for name in lists:
#     print(name)

# '''3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
# person’s name.'''

# lists = ['Sushil', 'Sunil', 'Srijan', 'Prashant','Ram']
# for name in lists:
#     print(f"Hello {name}")



# """3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
# """
# lists = ['Car', 'Bike', 'Bus', 'Aeroplane']
# print(f'I would like to own a Honda {lists[-3]}')


# '''The following exercises are a bit more complex than those in Chapter 2, but
# they give you an opportunity to use lists in all of the ways described.

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list thatt least includes a three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.'''

# lists = ['Sushil', 'Sunil', 'Samir']
# for name in lists:
#     print(name)
#     print(f"\tI would like to invide {name} to dinnner.")




# """3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.
# """
# lists = ['Sushil', 'Sunil', 'Samir']
# who_cant_makeittodinner = 'Sunil'
# lists.remove('Sunil')
# lists.append('Ranjit')
# for name in lists:
#     print(name)
#     print(f"\tI would like to invide {name} to dinnner.")


# '''3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.'''

# lists = ['Sushil', 'Sunil', 'Samir']
# who_cant_makeittodinner = 'Sunil'
# lists.remove('Sunil')
# lists.append('Ranjit')
# lists.insert(2, 'Suman')
# lists.insert(0, "Ramey")
# lists.append('Syamey')
# for name in lists:
#     print(name)
#     print(f"\tI would like to invide {name} to dinnner.")

'''3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.'''

lists = ['Sushil', 'Sunil', 'Samir']
who_cant_makeittodinner = 'Sunil'
lists.remove('Sunil')
lists.append('Ranjit')
lists.insert(2, 'Suman')
lists.insert(0, "Ramey")
lists.append('Syamey')
print("You can invite only two people for dinner.")

while 2<len(lists):
    removed_lists = lists.pop()
    print(removed_lists)
    print(f"\tSorry you can't come to dinner {removed_lists}")


for name in lists:
    print(name)
    print(f"\t{name}, You are still invited to dinner")

del lists[0:]
print(lists)
# # Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive.

# for i in range(1,21):
#     print(i)


# '''Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.'''

# number = list(range(1, 1000001))
# for i in number:
#     print(i)



# '''Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers'''

# number = [i for i in range(1,1000001)]
# print(min(number))
# print(max(number))
# print(sum(number))


# '''Use the third argument of the range() funcmbetion to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.'''

# a = [i for i in range(1,21,2)]
# for b in a:
#     print(b)

# """ Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list."""

# list = []
# for i in range(1,31):
#     if i%3==0:
#         list.append(i)
# print(list)

# # By using list comprehension for same quesiton
# list = [i for i in range(1,31) if i%3==0]
# print(list)

# '''A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube'''

# list  = [i**3 for i in range(1,11)]
# for j in list:
#     print(j)


# '''Cube Comprehension: Use a list comprehension to generate a list of the first
# 10 cubes.'''

# list = [i**3 for i in range(1,11)]
# print(list)