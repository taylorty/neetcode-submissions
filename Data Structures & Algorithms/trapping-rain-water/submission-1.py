class Solution:
    def trap(self, height: List[int]) -> int:
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
        return result