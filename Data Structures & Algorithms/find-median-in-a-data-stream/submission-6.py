class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if not self.min_heap or num <= self.min_heap[0]:
                heapq.heappush_max(self.max_heap, num)
            else:
                n = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush_max(self.max_heap, n)
        else:
            # max + 1 == min / max > min
            if self.max_heap[0] <= num:
                heapq.heappush(self.min_heap, num)
            else:
                n = heapq.heappop_max(self.max_heap)
                heapq.heappush_max(self.max_heap, num)
                heapq.heappush(self.min_heap, n)

    def findMedian(self) -> float:
        l = self.max_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return l
        r = self.min_heap[0]
        return (l + r) / 2
        
        