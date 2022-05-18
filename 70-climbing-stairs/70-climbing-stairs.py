class Solution:
    def climbStairs(self, n: int) -> int:
        
        counter = 0
        memo = {}
        def dfs(num, counter):
            counter += 1
            if num <= 2:
                if num == 1 or num == 2:
                    return num
                return 0
            if num in memo:
                return memo[num]
            fir = dfs(num - 2, counter)
            sec = dfs(num - 1, counter)
            
            memo[num] = fir + sec
            return memo[num]
        
        return dfs(n, 0)