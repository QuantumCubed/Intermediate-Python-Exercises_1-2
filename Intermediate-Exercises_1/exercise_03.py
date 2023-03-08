from collections import Counter


def count_lower(usr_str):

    char_array = list(usr_str.lower().strip())

    if char_array.__contains__(' '):
        char_array.remove(' ')

    return Counter(char_array)


word = input("Enter a string: ")

returned_dict = dict(count_lower(word))

print(returned_dict)
