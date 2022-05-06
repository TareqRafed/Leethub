class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        maxSum = 0
        
        while l < r:
            maxSum = max(min(height[l], height[r]) * (r - l), maxSum)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return maxSum