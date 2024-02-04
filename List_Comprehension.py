# Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive.

for i in range(1,21):
    print(i)


'''Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.'''

number = list(range(1, 1000001))
for i in number:
    print(i)



'''Summing a Million: Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers'''

number = [i for i in range(1,1000001)]
print(min(number))
print(max(number))
print(sum(number))


'''Use the third argument of the range() funcmbetion to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.'''

a = [i for i in range(1,21,2)]
for b in a:
    print(b)

""" Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list."""

list = []
for i in range(1,31):
    if i%3==0:
        list.append(i)
print(list)

# By using list comprehension for same quesiton
list = [i for i in range(1,31) if i%3==0]
print(list)

'''A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube'''

list  = [i**3 for i in range(1,11)]
for j in list:
    print(j)


'''Cube Comprehension: Use a list comprehension to generate a list of the first
10 cubes.'''

list = [i**3 for i in range(1,11)]
print(list)