# Using for loop
def forloop():
    print("Prints Natural numbers from 1 to 10")
    for i in range(10):  # Here, i gets value from 1 to 10
        print(i, end="   ")

    print("\nThis prints the individual elements of the string: ")
    for i in "Data set":  # Here, i gets elements of the string consecutively
        print(i, end="   ")

    print("\nThis prints the individual elements of the array: ")
    # Here, i gets the elements of the array
    sequence = ['hello', 1, 'a', 65, -23]
    for i in sequence:
        print(i, end="   ")

    print("\nThis uses enumerate to get elements from the sequence : ")
    # Enumerate takes a array and returns pairs of [index, element]
    for i, value in enumerate(sequence, start=1):
        print(i, value)

    print("\nThis prints the series from 1 to 20 with increasing value of 2")
    for i in range(1, 20, 2):
        print(i, end=" ,")

    # _, can be used instead of 'i' when not used for further operations
    print("\n Usecase of throwaway variable")
    for _ in range(10):
        print("Hello, Im currently being used as a throw-away Variable...")


# Using while loop
def whileloop():
    x = 1
    sum_ = 0
    while x <= 5:
        print(x, end=" + ")
        sum_ += x
        x += 1

    print(sum_)


# Taking values until even
def user():
    x = 1
    while x % 2 != 0:
        x = int(input("Enter an even value: "))
        if x % 2 == 0:
            print("You've cracked the code!!!")


user()
