# 19.Write a Python class to find validity of a string of parentheses, '(',  ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example
# "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

# Python3 code to Check for
# balanced parentheses in an expression
open_parentheses = ["[", "{", "("]
close_parentheses = ["]", "}", ")"]


def parentheses_validity(my_string):
    stack = []
    for i in my_string:
        if i in open_parentheses:
            stack.append(i)
        elif i in close_parentheses:
            pos = close_parentheses.index(i)
            if ((len(stack) > 0) and
                    (open_parentheses[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Invalid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"


# Driver code
test_string = "()[]{}"
print(test_string, "-", parentheses_validity(test_string))

test_string = "[)"
print(test_string, "-", parentheses_validity(test_string))

test_string = "({[()]"
print(test_string, "-", parentheses_validity(test_string))
