class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]
        max_val = 1
        min_val = 1
        res = max(nums)
        if max_val == 0 or min_val == 0:
            max_val = 1
            min_val = 1
        for i in range(0, len(nums)):
            
            if nums[i] == 0:
                max_val = 1
                min_val = 1
                continue
            
            
            oldMax = nums[i] * max_val  
            max_val = max(nums[i], nums[i] * max_val, nums[i] * min_val)
            min_val = min(nums[i], nums[i] * min_val, oldMax)
            print(max_val, min_val, nums[i])
            #print()
            res = max(max_val, res)
            
        return res