#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_values = sorted(a_dictionary.items())
    n = len(new_values)
    for key, value in new_values:
        print('{}: {}'.format(key, value))
