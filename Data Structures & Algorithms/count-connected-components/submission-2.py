class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(adj, prev, curr, visit):
            if curr in visit:
                return
            visit.add(curr)
            for neighbor in adj[curr]:
                if prev == neighbor:
                    continue
                dfs(adj, curr, neighbor, visit)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(adj, -1, i, visit)
                res += 1
        return res
