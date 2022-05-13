class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for index, val in enumerate(strs):
            key = ''
            for letter in sorted(val):
                key += letter
            if key in hmap:
                hmap[key].append(val)
            else:
                hmap[key] = [val]
        
        ans = []
        for val in hmap.values():
            ans.append(val)
        
        return ans