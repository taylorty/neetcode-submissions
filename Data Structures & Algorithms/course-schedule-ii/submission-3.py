class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        q = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                q.append(i)
        visited = []
        while q:
            curr = q.popleft()
            visited.append(curr)

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                # if nei not in visited:
        if len(visited) != numCourses:
            return []
        return visited
