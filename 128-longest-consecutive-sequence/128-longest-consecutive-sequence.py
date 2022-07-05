class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        best = 0
        
        for n in nums:
            streak = 0
            lookUp = n - 1
            if lookUp not in nums:
                lookUp += 1
                while lookUp in nums:
                    lookUp += 1
                    streak += 1
            
            best = max(streak, best, 1)
        
        return best