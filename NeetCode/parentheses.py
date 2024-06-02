# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

s = "[]"
def isValidParentheses(s):

    map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char not in map:
            stack.append(char)
            continue
            # stack = ['[']

        if not stack or stack[-1] != map[char]:
            return False
        else:
            stack.pop()

    return not stack

print(isValidParentheses(s))
