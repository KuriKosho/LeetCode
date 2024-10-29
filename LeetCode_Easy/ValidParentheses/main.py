def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:  # Check for validity
                return False
            stack.pop()  # Valid match, pop the opening bracket

    return not stack  # Return True if stack is empty, else False

# Test cases
print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False