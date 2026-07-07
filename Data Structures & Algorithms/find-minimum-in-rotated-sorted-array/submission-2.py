class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            m = (e - s) // 2 + s
            # The right half is out of order
            if nums[m] > nums[e]:
                s = m + 1
            elif nums[m] < nums[e]:
                e = m # m could be the minimum itself 

        return nums[s]
