class Solution:
    def numDecodings(self, s: str) -> int:
        cache = { len(s) : 1}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            if s[i] == '0':
                return 0
            
            count = dfs(i + 1)
            
            if (i + 1 < len(s) and int(s[i] + s[i+1]) <= 26):
                count += dfs(i + 2)
            
            cache[i] = count
            return cache[i]
        return dfs(0) 