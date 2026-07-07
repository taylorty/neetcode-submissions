class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[b].append(a)
            indegree[a] += 1
        
        start = []
        for i, num in enumerate(indegree):
            if num == 0:
                start.append(i)
                # break

        def dfs(start):
            
            if graph[start] == []:
                return True
            if start in visited:
                return False
            visited.add(start)
            for nextCourse in graph[start]:
                if not dfs(nextCourse):
                    return False
            visited.remove(start)
            graph[crs] = []
            return True
                # indegree[nextCourse] -= 1
                # dfs(nextCourse, visited)
        visited = set() # Tracks courses along the current DFS path
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        # for i in start:
        #     dfs(i, set())
        # # print(indegree)
        # for i in indegree:
        #     if i != 0:
        #         return False
        return True
