class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        ans = []
        for key, val in c.items():
            bucket[val].append(key)
        
        for arr in reversed(bucket):
            for val in arr:
                ans.append(val)
                if len(ans) == k:
                    return ans
        
        
        