class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        edges = defaultdict(list)
        
        for s, d, p in flights:
            edges[s].append((d, p))
        
        queue = collections.deque([(0, src, 0)])
        cheapest = float('inf')
        visit = defaultdict(lambda: float('inf'))
        while queue:
            price, node, stops = queue.popleft()
            
            
            if node == dst and stops - 1 <= k:
                cheapest = min(cheapest, price)
            
            
            if price > visit[node]:
                continue
            else:
                visit[node] = price
            
            if price < cheapest and stops - 1 <= k:
                for dist2, price2 in edges[node]:
                    queue.append((price2 + price, dist2, stops + 1))
        
        
        return cheapest if cheapest != float('inf') else -1