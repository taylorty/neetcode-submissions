class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        scores = [0] * (n + 1)
        for p1, p2 in trust:
            scores[p1] -= 1
            scores[p2] += 1
        for i, score in enumerate(scores):
            if score == n - 1:
                return i
        return -1

                
