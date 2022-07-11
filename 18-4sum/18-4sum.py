class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        
        def kSum(k, start, trgt):
            
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, trgt - nums[i])
                    quad.pop()
                return
            
            l, r = start, len(nums) - 1
            
            while l < r:
                t_sum = nums[l] + nums[r]
                if t_sum == trgt:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif t_sum < trgt:
                    l += 1
                
                else:
                    r -= 1
        
        kSum(4, 0, target)
        return res