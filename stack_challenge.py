# Challenge:
# Use stack to find if a string of brackets is balanced or unbalanced
# Example of a balanced ({[[{{{((()))}}}]]})


class Stack:

    def __init__(self):
        self.items = []

    # All methods have O(n) - constant time complexity

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    # len() has O(1) constant time complexity,
    # because the length of the list is stored in memory and the computer just needs to look it up.
    # The computer keeps track of the beginning and the end of the list (with the length)

    def lenght(self):
        return len(self.items)


def match_symbols(symbol_str):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:  # The symbol is a closer

            # If the Stack is already empty, the symbols are not balanced
            if my_stack.is_empty():
                return False

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True

    return False  # Stack is not empty so symbols were not balanced


print(match_symbols('([{}])'))
print(match_symbols('(([{}]])'))

# Testing my own method added to the stack
test_stack = Stack()

test_stack.push('(')
test_stack.push('(')
test_stack.push('(')

print(test_stack.lenght())
