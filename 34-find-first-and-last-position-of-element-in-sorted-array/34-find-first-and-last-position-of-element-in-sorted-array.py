class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        ans = []
        arr1 = nums[0: int((numsLen/2))]
        arr2 = nums[int(numsLen/2) : numsLen]
        
       
        
        #for i, val in enumerate(nums):
        l, r, m = 0, numsLen - 1, int(numsLen / 2)
        
        if numsLen == 0:
            return [-1, -1]
        
        while l <= r:
            m = (l + r) // 2
            if (r - l == 1 or r == l) and nums[l] != target and nums[r] != target:
                ans = [-1, -1]
                break
            if nums[m] > target:
                r = m - 1
                continue
            if nums[m] < target:
                l = m + 1
                continue
            if nums[m] == target:
                c = m
                while c >= 0 and nums[c] == target: 
                    c -= 1
                ans.append(c+1)
                c = m
                while c + 1 <= numsLen and nums[c] == target:
                    c += 1
                ans.append(c-1)
                break
            
                
                            
        
        return ans
        
        
            