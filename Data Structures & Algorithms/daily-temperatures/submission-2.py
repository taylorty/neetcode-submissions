class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if not stack:
                res.insert(0, 0)
            else:
                res.insert(0, stack[-1][1] - i)
            stack.append((temperatures[i], i))
                
        return res