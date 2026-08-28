class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            heapq.heappush_max(heap, (x * x + y * y, [x, y]))
            if len(heap) > k:
                heapq.heappop_max(heap)
        result = []
        m = heapq.heappop_max(heap)
        result.append(m[1])
        while heap:
            m = heapq.heappop_max(heap)
            result.append(m[1])
        return result