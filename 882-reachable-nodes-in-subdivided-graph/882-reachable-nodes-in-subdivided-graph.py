class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        visited = [False]*n
        nei = [ [] for _ in range(n)]
        
        for u,v,cnt in edges:
            nei[u].append((v,cnt))
            nei[v].append((u,cnt))
        
        newreached = defaultdict(int)
        
        minHeap = [(0,0)] # distance, node
        while minHeap:
            
            dist, node = heappop(minHeap)
            
            if visited[node]: 
                continue
            visited[node] = True
            
            moves = maxMoves-dist
            
            if moves > 0:
                for v,cnt in nei[node]:
                    newreached[(node,v)] = min(cnt, moves)
                    if not visited[v] and moves >= cnt+1:
                        heappush(minHeap, (dist+cnt+1,v))
        
        S = sum(visited) 
        for u,v,cnt in edges:
            S += min(cnt,newreached[(u,v)]+newreached[(v,u)])
        return S