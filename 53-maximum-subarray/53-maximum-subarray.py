class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        li = []
        maxSum = 0
        maxxedVal = float('-inf')
        for i, val in enumerate(nums):
            if i > 0 and nums[i - 1] < nums[i] and nums[i] > maxSum + nums[i]:
                maxSum = nums[i]
            else:
                maxSum += nums[i]
            
            maxxedVal = max(maxSum, maxxedVal)
        
        
        return maxxedVal