class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_val = max(count.values())
        result = [[] for i in range(max_val)]
        for key in count:
            val = count[key]
            result[val - 1].append(key)

        final = []
        print(result[::-1])
        for bucket in result[::-1]:
            
            if k > 0:
                for item in bucket:
                    k -= 1
                    final.append(item)

        return final

