proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
def check_separator(string):
    if ',' in string:
        return "comma"
    elif ';' in string:
        return "semicolon"
    elif ' ' in string:
        return "space"
    else:
        return "unknown"


for i, s in enumerate(strings):
    separator = check_separator(s)
    print(f"String {i+1} is separated by {separator}.")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
def process_comma_separated(string):
    items = string.split(',')
    items.reverse()
    return ','.join(items)



# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
def process_semicolon_separated(string):
    items = string.split(';')
    items.sort()
    return ','.join(items)



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
def process_space_separated(string):
    items = string.split(' ')
    items.sort(reverse=True)
    return ' '.join(items)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
def process_comma_space_separated(string):
    items = [item.strip() for item in string.split(',')]
    items.reverse()
    return ','.join(items)

for i, s in enumerate(strings):
    separator = check_separator(s)
    if separator == "comma":
        result = process_comma_separated(s)
    elif separator == "semicolon":
        result = process_semicolon_separated(s)
    elif separator == "space":
        result = process_space_separated(s)
    elif separator == "comma space":
        result = process_comma_space_separated(s)
    else:
        result = "Unknown separator"
    
    print(f"Processed String {i+1}: {result}")