#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) == 0:
        return []
    even_num_list = [num for num in num_list if num % 2 == 0]
    return even_num_list

def make_exclamation(sentence_list):
    exclamation_sentence_list = [word + '!' for word in sentence_list]
    return exclamation_sentence_list

print(return_evens([0,1,2,3,4,5,6,7,8,9]))