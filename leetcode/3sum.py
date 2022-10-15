
def threeSum(nums):
    res = []
    nums.sort()
    
    def twoSum():
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                
    
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1]  != nums[i]:
            twoSum()
            
    return res

def threeSumHash(nums):
    res = []
    nums.sort()
    
    def twoSumHash():
        seen = set()
        j = i + 1
        
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                    j += 1
            seen.add(nums[j])
            j += 1
                
    
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1]  != nums[i]:
            twoSumHash()
            
    return res