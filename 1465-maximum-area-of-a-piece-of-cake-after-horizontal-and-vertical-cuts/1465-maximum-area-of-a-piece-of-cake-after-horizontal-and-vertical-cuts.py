class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        verticalCuts.append(w)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        horizontalCuts.append(0)
        verticalCuts.sort()
        horizontalCuts.sort()
        ver = 0
        hori = 0
        for i in range(1, len(verticalCuts)):
            ver = max(verticalCuts[i] - verticalCuts[i - 1], ver)
            
        
        for i in range(1, len(horizontalCuts)):
            hori = max(horizontalCuts[i] - horizontalCuts[i - 1], hori)
        
        
        return (hori * ver) % 1000000007