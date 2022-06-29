class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, num * -1) # max heap
        
        if (self.left and self.right and (-1 * self.left[0]) > self.right[0]):
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)
        
        if (len(self.left) > len(self.right) + 1):
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)
        
        if (len(self.right) > len(self.left) + 1):
            val = heapq.heappop(self.right) * -1
            heapq.heappush(self.left, val)
            

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (self.right[0] + (self.left[0] * -1)) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()