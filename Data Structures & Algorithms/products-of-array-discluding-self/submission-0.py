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
        for num in nums[::-1]:
            right.append(prodR)
            prodR *= num
        # print(right)
        right = right[::-1]
        for i in range(len(left)):
            right[i] *= left[i]
        return right
        