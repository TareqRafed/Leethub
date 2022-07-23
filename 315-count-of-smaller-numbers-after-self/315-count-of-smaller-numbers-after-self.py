from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        res = SortedList()
        output = []
        for val in nums[::-1]:
            ans = SortedList.bisect_left(res, val)
            res.add(val)
            output.append(ans)
        
        return reversed(output)