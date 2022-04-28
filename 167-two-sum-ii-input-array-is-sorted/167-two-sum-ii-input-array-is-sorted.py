class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                ans.append(l + 1)
                ans.append(r + 1)
                break
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
            
        return ans