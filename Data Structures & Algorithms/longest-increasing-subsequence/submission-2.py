class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        length = [1] * n

        maxLen = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    length[i] = max(length[j] + 1, length[i])

            maxLen = max(maxLen, length[i])

        return maxLen