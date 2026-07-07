class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones:
            a = -heapq.heappop(stones)
            if not stones:
                return a
            b = -heapq.heappop(stones)

            heapq.heappush(stones, -abs(a - b))