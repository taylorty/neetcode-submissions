class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        s = 0
        l = len(nums) + 1
        while j < len(nums):
            s += nums[j]
            while s >= target:
                l = min(l, j - i + 1)
                s -= nums[i]
                i += 1
            j += 1
        if l == len(nums) + 1:
            return 0
        return l