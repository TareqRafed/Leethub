class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)
        
        for source, dist, wei in times:
            edges[source].append((dist, wei))
        
        queue = collections.deque([(0, k)])
        visit = set()
        t = [0] + [float('inf')] * n
        while queue:
            weight, source = queue.popleft()

            if weight < t[source]:    
                t[source] = weight
                for dist, wei in edges[source]:
                    queue.append((wei + weight, dist))
        
        return max(t) if max(t) != float('inf') else -1
            
        

       