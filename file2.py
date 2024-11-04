import random

def add(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mult(a, b):
    return a * b 

def div(a, b):
    if (b == 0):
        return -1; # error, cannot divide by 0
    return a + b 

def roll_dice():
    return random.randint(1, 6)
