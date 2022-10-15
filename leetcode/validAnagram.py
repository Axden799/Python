from collections import defaultdict

def isAnagram(s, t) -> bool: #O(n^2) complexity
    if len(s) != len(t):
        return False
    list_s = list(s)
    for c in t:
        if c not in list_s:
            return False
        else:
            list_s.remove(c)
    return True if not list_s else False

def isAnagramSortedSolution(s, t) -> bool: #O(nlogn) complexity since comparison sorting takes O(nlogn) time
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def isAnagramDictSolution(s, t,) -> bool: 
    '''
        O(3n) since we must parse s and t separately and 
        parse thru the values of the dictionary. 
        This means the complexity is O(n)
    '''
    my_dict = defaultdict(int)

    for char in s:
        my_dict[char] += 1
    
    for char in t:
        if char not in my_dict.keys():
            return False
        my_dict[char] -= 1
    
    for count in my_dict.values():
        if count != 0:
            return False
    
    return True


tests = {
    'test1': {
        's': 'anagram',
        't': 'nagaram',
        'expected': True
    }
}

for test in tests.values():
    response = isAnagramDictSolution(test['s'], test['t'])
    result = True if test['expected'] == response else False
    print(f"response: {response}, result: {result}")