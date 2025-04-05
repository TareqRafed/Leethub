# [1, 15, 7, 9, 2, 5, 10] # k = 3
# [1] i = 0
# [15, 15] i = 1
# [15, 15, 15] i = 2
# [15] i = 2
# [15, 15] i = 1
# [15, 15, 15] i = 1


# [1, 15, 7] [9] [2, 5, 10]
# [16,] [9] [17]
# ?? -> 
# [1, 15, 7]
# 
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            curMax = res = 0
            for j in range(i, min(i+k, n)):
                curMax = max(arr[j], curMax)
                window = j-i + 1
                curSum = curMax * window
                res = max(dfs(j+1) + curSum, res)
            memo[i] = res
            return res

        return dfs(0)
            
            
