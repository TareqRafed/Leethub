class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        visited = {}
        if len(nums) == 1:
            return True
        while i < len(nums) - 1:
            if i < 0:
                    return False
            if nums[i] == 0 and i not in visited:
                i -= 1
                if i in visited and i <= 0:
                    return False
            elif nums[i] == 0:
                return False
            else:
                if i in visited:
                    i -= 1
                else :
                    visited[i] = True
                    i+= nums[i]
            
        return True
            
