class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result

        """
        leftMax = []
        rightMax = []
        result = 0
        for h in height:
            if not leftMax:
                leftMax.append(h)
            else:
                leftMax.append(max(leftMax[-1], h))
        for h in height[::-1]:
            if not rightMax:
                rightMax.append(h)
            else:
                rightMax.append(max(rightMax[-1], h))
        
        rightMax = rightMax[::-1]
        # print(leftMax)
        # print(rightMax)
        for i in range(len(height)):
            result += min(leftMax[i], rightMax[i]) - height[i]
        """
        return result