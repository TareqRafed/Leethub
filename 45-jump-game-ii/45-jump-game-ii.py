class Solution:
    def jump(self, nums: List[int]) -> int:
        
        nums[-1] = 0
        
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] + i >= len(nums) - 1:
                nums[i] = 1
                continue
            
            
            temp = nums[i]
            nums[i] = float('inf')
            
            for j in range(i + 1, i + temp + 1):
                nums[i] = min(nums[j], nums[i])
            
            nums[i] += 1
            
        return nums[0]