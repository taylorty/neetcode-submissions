class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for num in arr:
            heapq.heappush_max(pq, (abs(x - num), num))
            if len(pq) > k:
                heapq.heappop_max(pq)
        return sorted([num for _, num in pq])

        l, r = 0, len(arr) - k
        
        while l < r:
            m = (l + r) // 2
            if arr[m] - x < arr[m + k] - x:
                l = m + 1
            else:
                r - m - 1

        return arr[l: l + k]