def wordBreak(s, wordDict):
    n = len(s)
    word_dict = set(wordDict)
        
    @lru_cache(None)
    def dp(start):
        if start == n:
            return True
        for end in range(start+1, n+1):
            word = s[start:end]
            if word in word_dict and dp(end):
                return True
        return False
    return dp(0)

def wordBreakTabulation(s, wordDict):
    n = len(s)
    wordSet = set(wordDict)
    dp = [False] * (n + 1)
    dp[n] = True
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if s[i:j] in wordSet and dp[j]:
                dp[i] = True
                break
    return dp[0]