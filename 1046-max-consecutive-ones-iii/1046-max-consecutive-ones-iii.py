# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

# checkpoint: 2
# 1 -> 1 -> 1 -> 1 -> 1 
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        count = 0
        max_count = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                num_zeros += 1
            while num_zeros > k and i < len(nums):
                if nums[i] == 0:
                    num_zeros -= 1
                count -= 1
                i += 1
            
            count += 1
            j+=1
            max_count = max(count, max_count)
            
        
        return max_count

# 0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1