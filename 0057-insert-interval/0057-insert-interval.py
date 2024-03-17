class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        i = 0
        
        while i < len(intervals):
            if i == 0:
                i += 1
                continue
            if intervals[i][0] <= intervals[i - 1][1]:
                if intervals[i][1] > intervals[i - 1][1]:
                    intervals[i - 1][1] = intervals[i][1]
                intervals.pop(i)
                continue
            
            
            
            i += 1
        
        return intervals

## [1,5] [2,5] [6,9]

##[[1,2],[3,5], [4,8],[6,7],[8,10],[12,16]]
## [4,8]

##[[1,2],[3,10],[12,16]]
## [4,8]