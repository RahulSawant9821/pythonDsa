'''Intermediate:  Write a program that checks if a given input word is a palindrome (reads the same backward as forward) using tuple techniques. (e.g., "racecar" is a palindrome)'''

user_input = input("Enter the value to be checked for palindrome :")

input_tuple = tuple( user_input)

reversed_tuple = input_tuple[::-1]

if input_tuple == reversed_tuple:
    print("Palindrome")
else:
    print("Not a palindrome")