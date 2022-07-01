class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: (-x[1], -x[0]))
        c = truckSize
        res = 0 
        for box in boxTypes:
            if c == 0:
                return res
            if c - box[0] >= 0:
                c -= box[0]
                res += box[0] * box[1]
            else:
                res += box[1] * c
                c = 0
        
        return res