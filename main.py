# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        elif next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return 0

def main():
    #input_type = input("Choose '0-5' to select a test or 'I' to input brackets: ")
    #if input_type.isdigit() and int(input_type) in range(6):
        #test_number = input_type
        #test_path = "/workspaces/steks-un-iekavas-DanielsPots/test/" + test_number
        #with open (test_path, "r") as f:
            #text = f.read()
    input_type = input()
    if input_type == "I":
        text = input("Enter brackets: ")
    else:
        text = input()
        return

    mismatch = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
         print(mismatch)
    

if __name__ == "__main__":
    main()
