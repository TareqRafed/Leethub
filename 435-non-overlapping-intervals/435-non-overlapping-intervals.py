class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals):
            if s >= end: 
                end = e
            else: 
                cnt += 1
                end = min(end, e)
        return cnt
    
    