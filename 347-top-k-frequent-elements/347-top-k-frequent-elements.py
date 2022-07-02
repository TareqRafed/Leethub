class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        ans = []
        for key, val in c.items():
            ans.append((key, val))
        
        ans.sort(key = lambda x: -x[1])
        ans = list(map(lambda x: x[0], ans)) 
        return ans[:k]
        
        
        