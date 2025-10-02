import random

listy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    random.seed(42)  # Set a fixed seed
    state1 = random.getstate()
    print("Random number between 0 and 1: ", random.random())
    print("Random number between 1 and 10: ", random.randint(1, 10))
    print("Random number between 100 and 1000: ", random.randint(100, 1000))
    print("Random number between 1000 and 10000: ", random.randint(1000, 10000))
    print("Random number between 1 and 100 with step of 5: ",
          random.randrange(1, 100, 5))
    print("Random choice from a list: ", random.choice(listy))
    print("Random sample of 5 from a list: ", random.sample(listy, 5))
    random.shuffle(listy)
    print("Shuffled list: ", listy)
    print("The state has been changed...")
    x = input("Do you want to return to initial state? (y/n): ").lower()
    if x != 'y':
        print("Exiting without changing state...")
        return
    else:
        random.setstate(state1)
        print("State changed to initial state.")


if __name__ == "__main__":
    main()
