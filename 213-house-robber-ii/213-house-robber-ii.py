class Solution:
    def rob(self, nums: List[int]) -> int:
        
       
        
        
        def helper(nums):
            rob1, rob2 = 0, 0
            
            for val in nums:
                newRob = max(rob1 + val, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        
        return max(helper(nums[0:len(nums) - 1]), helper(nums[1:])) if len(nums) > 1 else nums[0]