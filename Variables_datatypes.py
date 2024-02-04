'''2-1. Simple Message: Assign a message to a variable, and then print that
message.'''

a = 'Hello World'
print(a)


'''2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.'''

a  = "Sinsail"
print(f"Hello {a},")
a = "Ayuzz"
print(f"Hello {a},")


'''2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”'''

name = "Sinsail"
print(f"Hello {name}, would you like to learn some Python today?")


'''2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.'''

name = "Sinsail"
print(name.upper())
print(name.lower())
print(name.title())


'''2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.”'''

Author = "Albert Einstein"
Quote = 'A person who never made a mistake never tried anything new.'
print(f"{Author} once said, '{Quote}'")


'''2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.'''

Author = "Albert Einstein"
Quote = 'A person who never made a mistake never tried anything new.'
message = f"{Author} once said, '{Quote}'"
print(message)



'''2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().'''

name = "    Sunil Shah  "
print(len(name))
print(name.rstrip())
print(name.lstrip())
print(f"His name is: \n \t\t{name.strip()}")

'''2-8. File Extensions: Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do'''

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

"""2-9. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8 your op. Be sure to encloseerations
in print() calls to see the uld creatresults. You shoe four lines that look like this:
print(5+3)
Your output should be four lines, with the number 8 appearing once on
each line."""

# Addition
print(5 + 3)

# Subtraction
print(10 - 2)

# Multiplication
print(4 * 2)

# Division
print(16 / 2)


"""2-10. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message."""

fav_number = 21
message = f"My favourite number is {fav_number}"
print(message)