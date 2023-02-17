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
        return "Success"

def main():
    input_type = input("Choose 'F' to select a test or 'I' to input brackets: ")
    if input_type == 'F':
        test_number = input("Enter test number (0-5): ")
        test_path = "/workspaces/steks-un-iekavas-DanielsPots/test/" + test_number
        with open (test_path, "r") as f:
            text = f.read()
    elif input_type == "I":
        text = input("Enter brackets: ")
    else:
        print("Invalid input type")
        return

    mismatch = find_mismatch(text)
    print(mismatch)
    

if __name__ == "__main__":
    main()
