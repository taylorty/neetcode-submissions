class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        for point in points:
            val = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
            heapq.heappush(self.heap, (-val, point))
            while len(self.heap) > k:
                if len(self.heap) == k:
                    return [result[1] for result in self.heap]
                heapq.heappop(self.heap)
            # print(self.heap)
        return [result[1] for result in self.heap]