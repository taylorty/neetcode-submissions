class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = []
        for val in nums:
            heapq.heappush(self.heap, val)
            while len(self.heap) > k:
                if len(self.heap) == k:
                    return self.heap[0]
                heapq.heappop(self.heap)
        return self.heap[0]