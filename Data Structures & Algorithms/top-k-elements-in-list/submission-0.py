class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            
        while len(heap) > k:
            heapq.heappop(heap)

        return [num for _, num in heap]
