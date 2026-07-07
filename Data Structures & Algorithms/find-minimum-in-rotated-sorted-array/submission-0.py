class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            m = (e - s) // 2 + s
            # 1. Check if the LEFT half is sorted
            if nums[m] > nums[e]:
                s = m + 1
            elif nums[m] < nums[e]:
                e = m                    

        return nums[s]
