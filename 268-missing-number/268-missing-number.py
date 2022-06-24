class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        arrSum = sum(nums)
        arrLen = len(nums)
        totalSum = 0
        for val in range(arrLen + 1):
            totalSum += val
        
        return totalSum - arrSum