class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        prod = 1
        for num in nums:
            left.append(prod)
            prod *= num
        prodR = 1
        # print(left)
        for i in range(len(nums) - 1, -1, -1):
            left[i] *= prodR
            prodR *= nums[i]
        # print(right)
        # right = right[::-1]
        # for i in range(len(left)):
        #     right[i] *= left[i]
        return left
        