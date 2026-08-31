class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i = 0
        result = 0
        heights.append(0)
        while i < len(heights):
            height = heights[i]
            if not stack or heights[stack[-1]] <= height:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > height:
                    left = stack.pop()
                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1

                    result = max(result, width * heights[left])
                stack.append(i)
            i += 1
        return result
