class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9 + 7
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                # Number of subsequences with nums[left] as the minimum
                res = (res + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1
                
        return res
