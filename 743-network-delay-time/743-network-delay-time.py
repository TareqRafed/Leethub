class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)
        
        for source, dist, wei in times:
            edges[source].append((dist, wei))
        
        heap = [(0, k)]
        visit = set()
        t = 0
        while heap:
            weight, source = heapq.heappop(heap)
            
            if source in visit:
                continue
            
            visit.add(source)
            
            t = max(t, weight)
            
            for dist, wei in edges[source]:
                heapq.heappush(heap, (wei + weight, dist))
    
        return t if len(visit) == n else -1
            
        

       