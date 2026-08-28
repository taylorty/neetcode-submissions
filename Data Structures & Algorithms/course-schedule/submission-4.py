class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        q = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                q.append(i)
        visited = set()
        while q:
            curr = q.popleft()
            visited.add(curr)

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                # if nei not in visited:

        return len(visited) == numCourses

        