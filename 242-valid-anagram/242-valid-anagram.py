class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hmap = defaultdict(lambda x: 0)
        
        for val in s:
            hmap[val] = hmap.get(val, 0) + 1
        
        for val in t:
            hmap[val] = hmap.get(val, 0) - 1
        
        
        for val in hmap.values():
            if val != 0:
                return False
        
        return True