def productExceptSelf(nums):
    length = len(nums)
    L, R, answer = [0]*length, [0]*length, [0]*length
    
    L[0] = 1
    R[length - 1] = 1
    
    for n in range(1, length):
        L[n] = nums[n - 1] * L[n - 1]
        
    for n in reversed(range(length - 1)):
        R[n] = nums[n + 1] * R[n + 1]
        
    for n in range(length):
        output[n] = L[n] * R[n]
        
    return output

def constantSpace(nums):
    length = len(nums)
    answer = [0] * len(nums)
    
    answer[0] = 1
    
    for n in range(1, length):
        answer[n] = nums[n-1] * answer[n - 1]
    
    R = 1
    for n in reversed(range(length)):
        answer[n] = answer[n] * R
        R *= nums[n]
        
    return answer

