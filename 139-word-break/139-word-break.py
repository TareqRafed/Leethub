class Trei:
    def __init__(self, val = '', nextLetter = None, isWord = False):
        self.val = val
        self.nextLetter = nextLetter
        self.isWord = isWord

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            
            
            for word in wordDict:
                currentWord = s[i:i+len(word)]
                if currentWord == word and i + len(word) <= len(s):
                    dp[i] = dp[i + len(word)]
                
                if dp[i]:
                    break
        
        return dp[0]
        
        
                    