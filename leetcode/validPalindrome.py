def isPalindrome(s) -> bool:
    lower_str = s.lower()
    final_str = re.sub('\W+|_', '', lower_str)
    if final_str == final_str[::-1]:
        return True
    else:
        False

def isPalindromeBetter(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
        
tests = {
    'test1': {
        's': "A man, a plan, a canal: Panama",
        'expected': True
    }
}

for test in tests.values():
    response = isPalindromeBetter(test['s'])
    result = True if response == test['expected'] else False
    print(f"response: {response}, result: {result}")