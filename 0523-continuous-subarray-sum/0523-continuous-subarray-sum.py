# nums = [23,2,4,6,7], k = 6
# [23,2,4,6,7]
# [25,6,10,13]
# [31,16,23]

# [25, 6, 10, 13]


# [23,2,6,4,7], k = 13

# [5, 0, 0, 0] k = 3

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_ind = {0:-1}
        acc = 0
        for i in range(len(nums)):
            num = nums[i]
            acc += num
            reminder = acc%k
            if reminder not in reminder_ind:
                reminder_ind[reminder] = i
            elif i - reminder_ind[reminder] >= 2:
                return True
        return False