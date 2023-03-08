#link to resource used: https://www.geeksforgeeks.org/python-difference-in-keys-of-two-dictionaries/

def get_combined_dict(dict_1, dict_2):
    #my_dict_3 = Counter(dict_1) + Counter(dict_2)

    my_dict_3 = {}
    dupes = set(dict_1.keys()).intersection(dict_2.keys()) #used w3schools for finding duplicate keys in multiple dictionaries

    for i in dupes:
        val = my_dict_1.get(i) + my_dict_2.get(i)
        my_dict_3.update({i: val})

    return my_dict_3


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

combined_dict = get_combined_dict(my_dict_1, my_dict_2)

print(combined_dict)
