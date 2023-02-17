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
    source = input("Choose 'F' to select a file or 'I' to input brackets: ")
    if source.lower() == 'f':
        file_path = input("Enter file path: ")
        try:
            with open(file_path, 'r') as f:
                text = f.read()
                mismatch = find_mismatch(text)
                print(mismatch)
        except FileNotFoundError:
            print("File not found")
    elif source.lower() == 'i':
        text = input("Enter brackets: ")
        mismatch = find_mismatch(text)
        print(mismatch)
    else:
        print("Invalid input. Choose 'F' or 'I'.")


if __name__ == "__main__":
    main()
