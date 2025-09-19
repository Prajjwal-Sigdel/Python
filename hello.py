# Getting input from the user
name = input("What is you name? ")

# remove whitespace of the string
name = name.strip()

# Capitalize the users name
name = name.capitalize()

# Split users name into first and second
first, last = name.split(" ")

# Printing normally using Python
print("Hello, World")

# Manipulating named Parameters of Print functions
print("Hello, ", end="\n\n")  # What to put at the end of the print function
print("world")

# What to put after every parameter seperations
print("Welcome to the chat,", last, sep="___")

# Printing formatted string
print(f"Hello , {first}")
