class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)
        res = 0
        while s < e: 
            m = (e - s) // 2 + s 
            
            if nums[m] < target:
                s = m + 1
            else:
                e = m

        return s