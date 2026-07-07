class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        res = 0
        for p, s in pair:
            t = (target - p) / s
            if not stack:
                
                stack.append(t)
                res += 1
            else:
                if t > stack[-1]:
                    res += 1
                    stack.append(t)
                # else:
                #     stack.append(t)
        return res