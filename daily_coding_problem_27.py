# Given a string of round, curly, and square open and closing brackets, return whether the brackets are
# balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.


def is_well_balanced(bracket_string):
    stack = []
    for c in bracket_string:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
        elif c == ']':
            if stack[len(stack)-1] != '[':
                return False
            else:
                stack.pop()
        elif c == ')':
            if stack[len(stack)-1] != '(':
                return False
            else:
                stack.pop()
        elif c == '}':
            if stack[len(stack)-1] != '{':
                return False
            else:
                stack.pop()
        else:
            return False
    if len(stack) != 0:
        return False
    return True


print is_well_balanced("([])[]({})")
print is_well_balanced("([)]")
print is_well_balanced("((()")
