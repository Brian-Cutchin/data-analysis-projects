my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[3:] + my_string[0:3]
print(new_string)


# Use a template literal to print the original and modified string in a descriptive phrase.
print(f'My old word is {my_string} but my new word is {new_string}')


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

x = int(input('Enter a number to relocate:'))
new_string = my_string[x:] + my_string[0:x]
print(new_string)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

x = int(input('Enter a number to relocate:'))

if len(my_string) < x:
    print("Error: Number of letters to relocate is too large.")
    x = 3

new_string = my_string[x:] + my_string[0:x]
print(f'My old word is {my_string} but my new word is {new_string}')
