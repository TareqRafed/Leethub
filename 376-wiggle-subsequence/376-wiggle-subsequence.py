class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)
        
        up = [0] * len(nums)
        down = [0] * len(nums)
        
        for i, val in enumerate(nums):
            for j, val2 in enumerate(nums):
                if val > val2:
                    up[i] = max(up[i], down[j] + 1) 
                elif val < val2:
                    down[i] = max(down[i], up[j] + 1)
        
        
        return max(down[-1], up[-1], 1)