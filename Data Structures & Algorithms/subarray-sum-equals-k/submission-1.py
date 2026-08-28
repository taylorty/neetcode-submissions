class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
        
            if curr_sum - k in prefixSum:
                count += prefixSum[curr_sum - k]

            if curr_sum not in prefixSum:
                prefixSum[curr_sum] = 1
            else:
                prefixSum[curr_sum] += 1

        # i = 0
        # j = 1
        # count = 0
        # print(prefixSum)
        # while j < len(prefixSum):
        #     if prefixSum[j] - prefixSum[i] == k:
        #         count += 1
        #         j += 1
        #     elif prefixSum[j] - prefixSum[i] > k:
        #         i += 1
        #     else:
        #         j += 1
        return count