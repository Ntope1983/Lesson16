from stack import Stack


def convert_10_to_2(number):
    if number == 0:
        return "0"
    number_stack = Stack()
    while number > 0:
        number_stack.push(number % 2)
        number = number // 2
    result = ""
    while number_stack.length() > 0:
        result += str(number_stack.pop())
    return result


print(convert_10_to_2(225))