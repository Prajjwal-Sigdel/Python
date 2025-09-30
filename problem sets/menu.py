menu = {
    "momo": 120,
    "chowmein": 100,
    "ice peach tea": 200,
    "pizza": 300,
    "burger": 140,
    "fries": 100
}


def food_menu():
    while True:
        try:
            food = input("Enter your order: ")
            print("The cost is: ", menu[food])
        except Exception as error:
            print("Error,", error)
            break


food_menu()
