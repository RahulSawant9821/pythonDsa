''' Intermediate:  Write a function that takes a tuple of strings and returns a new tuple with all the strings reversed. (e.g., ("hello", "world") -> ("olleh", "dlrow")) '''


def reverse_tuple(tuple_input):
    rev_tup = tuple(element[::-1] for element in tuple_input)

    print(rev_tup)
    



tuple_input = tuple(input("Enter the strings seperated by a comma : ").split(","))
reverse_tuple(tuple_input)