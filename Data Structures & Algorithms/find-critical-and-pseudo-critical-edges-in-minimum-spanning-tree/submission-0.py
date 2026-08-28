class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:

        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key=lambda x: x[2])

        def get_weight(in_index: int = -1, ex_index: int = -1):
            uf = UnionFind(n)
            weight = 0

            if in_index != -1:
                for u, v, w, orig_idx in edges:
                    if orig_idx == in_index:
                        if uf.union(u, v):
                            weight += w
                        break

            for u, v, w, orig_idx in edges:
                if orig_idx == ex_index:
                    continue

                if uf.union(u, v):
                    weight += w

            return weight if uf.count == 1 else float("inf")

        initial_weight = get_weight()

        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            orig_idx = edges[i][3]

            if get_weight(ex_index=orig_idx) > initial_weight:
                critical.append(orig_idx)
            elif get_weight(in_index=orig_idx) == initial_weight:
                pseudo_critical.append(orig_idx)

        return [critical, pseudo_critical]