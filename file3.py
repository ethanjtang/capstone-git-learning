import random

def string_to_uppercase(input_str): 
    return input_str.upper()

def string_to_lowercase(input_str): 
    return input_str.lower()

def scramble_string(input_str):
    # convert str to list
    char_list = list(input_str)
    
    # shuffle characters in list
    random.shuffle(char_list)
    
    # return scrambled string
    scrambled_string = ''.join(char_list)
    return scrambled_string
