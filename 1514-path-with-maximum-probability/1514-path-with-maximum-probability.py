class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        _edges = defaultdict(list)
        
        for index, (src, dist) in enumerate(edges):
            _edges[src].append((succProb[index], dist))
            _edges[dist].append((succProb[index], src))
        
        
        heap = [(-1, start)]
        visited = set()
        
        while heap:
            pro, node = heappop(heap)
            pro *= -1
            
            if node in visited:
                continue
            
            if node == end:
                return pro
            
            visited.add(node)
            
            for prob, dist in _edges[node]:
                
                heappush(heap, (-prob * pro, dist))
            
        return 0