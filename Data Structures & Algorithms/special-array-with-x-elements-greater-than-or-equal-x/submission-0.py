class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l <= r:
            m = l + (r - l) // 2
            count = sum(1 for num in nums if num >= m)
            if count == m:
                return m
            elif count > m:
                l = m + 1
            else:
                r = m - 1
        return -1