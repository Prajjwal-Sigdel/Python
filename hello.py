# Initilizing a buch of strings in an array
Shows = ["My name is jeff", "yeah buddy",
         " you don't know Me son", "the man of the house  "]

# defining a main function


def main():
    # Loop to get individual string from the array
    for show in Shows:
        print(show.strip().capitalize())

    # Defining a new array to store cleaned strings
    cleaned_Shows = []
    for show in Shows:

        # Adding respective elements to the new array
        cleaned_Shows.append(show.strip().title())

    # Displayig the new array of cleaned strings
    print(', '.join(cleaned_Shows))


# Calling main
main()

# All the string functions i learned
# .capitalize()--> First character of string is capitalized
# .title()--> Starting letters of all the words are capitalized
# .strip()--> Removes whitespaces from both left and right side of the string
# .append()--> Adds elemnts to the new array
# .join()--> Joining the elements of the array as desired
