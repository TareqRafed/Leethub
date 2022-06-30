class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        i, j = 0, len(nums) - 1
        m = (i + j) // 2
        res = 0
        for index, val in enumerate(nums):
            if index == m:
                continue
            
            if val != nums[m]:
                res += abs(val - nums[m])
        
        return res