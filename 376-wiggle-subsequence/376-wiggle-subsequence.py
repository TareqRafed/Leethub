class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)
        
        dp = [nums[i] - nums[i-1] for i in range(1, len(nums)) if nums[i] - nums[i - 1] != 0]
        
        if len(dp) == 0:
            return 1
        
        ans = 2
        for ind in range(1, len(dp)):
            if dp[ind] > 0 and dp[ind - 1] < 0 or dp[ind] < 0 and dp[ind - 1] > 0:
                ans += 1
        print(dp, ans)
        return ans