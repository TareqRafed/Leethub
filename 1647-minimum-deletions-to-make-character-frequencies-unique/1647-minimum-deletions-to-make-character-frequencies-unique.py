class Solution:
    def minDeletions(self, s: str) -> int:
        
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        pq = [-f for f in freq if f != 0]
        
        heapq.heapify(pq)
        
        delete_count = 0
        
        while len(pq) > 1:
            top_e = -heapq.heappop(pq)
            
            if top_e == -pq[0]:
                if top_e - 1 > 0:
                    top_e -= 1
                    heapq.heappush(pq, - top_e)
                
                delete_count += 1
        
        return delete_count
        
        