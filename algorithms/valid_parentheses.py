def is_valid_parentheses(text: str) -> bool:
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
            continue

        if not stack:
            return False

        if stack.pop() != pairs[char]:
            return False

    return not stack


assert is_valid_parentheses("()[]{}") is True
assert is_valid_parentheses("([{}])") is True
assert is_valid_parentheses("([)]") is False
assert is_valid_parentheses("(") is False
assert is_valid_parentheses("]") is False
assert is_valid_parentheses("") is True

print("所有测试通过")