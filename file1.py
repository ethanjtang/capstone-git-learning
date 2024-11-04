from file2 import add, sub, mult, div, roll_dice
from file3 import string_to_uppercase, string_to_lowercase, scramble_string

def main():
    # test arithmetic operations
    print("\nTesting arithmetic operations:")
    print(f"add(3, 4) = {add(3, 4)}")               # Should print 7
    print(f"sub(10, 4) = {sub(10, 4)}")             # Should print 6
    print(f"mult(3, 5) = {mult(3, 5)}")             # Should print 15
    print(f"div(10, 2) = {div(10, 2)}")             # Should print 12 (10 + 2)
    print(f"div(10, 0) = {div(10, 0)}")             # Should print -1 (error)
    print(f"roll_dice() = {roll_dice()}")           # Should print a number between 1 and 6

    # test string operations
    print("\nTesting string operations:")
    test_string = "Hello, World!"
    print(f"string_to_uppercase('{test_string}') = {string_to_uppercase(test_string)}")  # Should print 'HELLO, WORLD!'
    print(f"string_to_lowercase('{test_string}') = {string_to_lowercase(test_string)}")  # Should print 'hello, world!'
    print(f"scramble_string('{test_string}') = {scramble_string(test_string)}")          # Should print a scrambled version of 'Hello, World!'

if __name__ == "__main__":
    main()



