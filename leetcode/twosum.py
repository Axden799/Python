

def twoSum(nums, target):
    print(nums)
    print(target)
    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]

def improvedTwoSum(nums, target):
    all_nums = {}
    for idx in range(len(nums)):
        all_nums[nums[idx]] = idx

    print(f"DICT: {all_nums}")

    for idx in range(len(nums)):
        complement = target - nums[idx]
        if complement in all_nums.keys() and all_nums[complement] != idx:
            return [idx, all_nums[complement]]


tests = {
    'test_1':
    {
        'nums': [2, 7, 11, 15],
        'target': 9,
        'expected': [0, 1]
    }
}

tests['test_2'] = {
    'nums': [3,3],
    'target': 6,
    'expected': [0,1]
}

for test in tests.values():
    result = improvedTwoSum(test['nums'], test['target'])
    answer = True if result == test['expected'] else False
    print(f"result: {result} expected: {test['expected']}, correct?: {answer}")
    
print("DONE TESTING")
