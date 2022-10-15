from collections import Counter

def lengthOfLongestSubstring(s):
        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return 1
        longest_substring = 0
        s_list = list(s)
        
        for x in range(len(s_list)-1):
            count = 1
            chars_count = Counter()
            chars_count[s_list[x]] += 1
            
            for y in range(x+1, len(s)):
                chars_count[s_list[y]] += 1
                repeating_chars = False
                for counter in chars_count.values():
                    if counter > 1:
                        repeating_chars = True
                        break
                if repeating_chars: break
                count += 1
            if count > longest_substring:
                longest_substring = count
        
        return longest_substring

tests = {
    'test1': {
        's': 'abcabcbb',
        'result': 3
    }
}

for test in tests.values():
    response = lengthOfLongestSubstring(test['s'])
    result = False
    if response == test['result']:
        result = True
    print(result)