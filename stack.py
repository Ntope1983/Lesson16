# Removes and returns the last element (top of the stack), or None if empty
# Convert a number from binary representation 10 to 2 using stack
class Stack:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        if self.length() == 0:
            return None
        else:
            return self.array.pop()

    def length(self):
        return len(self.array)



