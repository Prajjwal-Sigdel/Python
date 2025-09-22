# Converts camelcase into snake_case
def camel():
    str_camel = input("camelCase: ")
    for i in str_camel:
        if i.isupper():
            print("_", i.lower(), sep="", end="")
        else:
            print(i, end="")


# Transaction process for 50 cent coke
def coke():
    amount = 50
    print("Amount Due:", amount)
    while amount > 0:
        insert_amount = int(input("Insert Coin: "))
        if insert_amount not in (25, 10, 5):
            insert_amount = 0
        amount -= insert_amount
        print("Amount Due:", abs(amount))


# Removes vowels from the given string
def vowel():
    string = input("INPUT: ")
    print("OUTPUT: ", end="")
    for i in string:
        if i.lower() not in ('a', 'e', 'i', 'o', 'u'):
            print(i, end="")


# Checks if the given input is valid for vanity plates
def vanity():

    # Get the input from the user
    string = input("Enter the plate: ")
    if check(string):
        print("Valid")
    else:
        print("Invalid")


def check(s):

    # Checks for the valid length of the given input
    if not (2 <= len(s) <= 6):
        return False

    # Checks for first two elements to be alphabets
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Checks  for invalid Characters
    if not s.isalnum():
        return False

    # Checks for numbers in input
    Found_digit = False
    for ch in s:
        if ch.isdigit():
            if not Found_digit:
                if ch == '0':
                    return False
                Found_digit = True
        else:
            if Found_digit:
                return False
    return True

# To get the caloric value of fruit consumed


def nutrition():

    # Define a dict with all the fruits as keys and calories as their respective calories
    Fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "grapefruit": 60,
        "grapes": 90,
        "lemon": 15,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapples": 50,
        "plums": 70,
        "watermelon": 80
    }
    # Input the fruit from the user
    Fruit = input("Enter the fruit: ").strip().lower()
    # Check and print the value for the keys that exist in the dict
    if Fruit in Fruits:
        print("Calories: ", Fruits[Fruit])


camel()
coke()
vowel()
vanity()
nutrition()
