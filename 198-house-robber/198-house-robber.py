class Solution:
    def rob(self, nums: List[int]) -> int:
        sum = float("-inf")
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            
            if index >= len(nums):
                return 0
            
            if index == len(nums) - 1 or index == len(nums) - 2:
                memo[index] = nums[index]
                return nums[index]
            
            
            
            memo[index] = max(dfs(index + 2), dfs(index + 3)) + nums[index]
            
            return memo[index]
        
        return max(dfs(0), dfs(1))