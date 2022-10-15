def isValid(s: str) -> bool:
    str_stack = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            str_stack.append(char)
        if char == ')' or char == ']' or char == '}':
            if not str_stack:
                return False
            elif str_stack[-1] == '(' and char == ')':
                str_stack.pop()
            elif str_stack[-1] == '[' and char == ']':
                str_stack.pop()
            elif str_stack[-1] == '{' and char == '}':
                str_stack.pop()
            else:
                return False
    return True if not str_stack else False

tests = {
    'test1': {
        's': ['(', '[', '{', '}', ']', ')'],
        'expected': True
    }
}

for test in tests.values():
    result = isValid(test['s'])
    answer = True if result == test['expected'] else False

    print(f"List: {test['s']} result: {result} answer: {answer}")