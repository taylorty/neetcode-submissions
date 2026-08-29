class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for num in arr:
            heapq.heappush_max(pq, (abs(x - num), num))
            if len(pq) > k:
                heapq.heappop_max(pq)
        return sorted([num for _, num in pq])