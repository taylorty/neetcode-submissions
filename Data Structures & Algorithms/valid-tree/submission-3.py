class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        # has cycle
        def dfs(adj, prev, curr, visit):
            if curr in visit:
                print(curr, visit)
                return False
            visit.add(curr)
            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue
                # if neighbor in visit:
                #     continue
                if not dfs(adj, curr, neighbor, visit):
                    return False

            return True

        if not dfs(adj, -1, 0, visit):
            return False
        return len(visit) == n
