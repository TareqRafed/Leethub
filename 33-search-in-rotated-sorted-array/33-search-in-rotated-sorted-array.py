class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target <= nums[r-1] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return -1