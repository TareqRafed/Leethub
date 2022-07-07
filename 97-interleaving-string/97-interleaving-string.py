class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        
        if len(s3) == 1 or len(s3) == 0:
            return s1 + s2 == s3 or s2 + s1 == s3 
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        @lru_cache(None)
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            first = None
            second = None
            if i < len(s1) and s1[i] == s3[i + j]:
                first = dfs(i + 1, j)

            
            if j < len(s2) and s2[j] == s3[i + j]:
                second = dfs(i, j + 1)

            
            return first or second
        
        return dfs(0, 0)