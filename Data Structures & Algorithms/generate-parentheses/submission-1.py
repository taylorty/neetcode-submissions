class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n, 0, 0, "", result)
        return result

    def dfs(self, n, left, right, curr, result):
        if left > n or right > n:
            return
        if left == n and right == n:
            result.append(curr)
            return
        
        if left < n:
            self.dfs(n, left + 1, right, curr + "(", result)
        if left > right:
            # self.dfs(n, left + 1, right, curr + "(", result)
            self.dfs(n, left, right + 1, curr + ")", result)
        