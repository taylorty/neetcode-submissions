class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # indegree = [0 for i in range(numCourses)]
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[a].append(b)
            # indegree[a] += 1
        
        # start = []
        # for i, num in enumerate(indegree):
        #     if num == 0:
        #         start.append(i)
                # break
        output = []
        visited = set() # Tracks courses along the current DFS path
        cycle = set()
        def dfs(start):
            
            if start in cycle:
                return False
            if start in visited:
                return True
            cycle.add(start)
            for nextCourse in graph[start]:
                if not dfs(nextCourse):
                    return False
            cycle.remove(start)
            visited.add(start)
            output.append(start)
            return True
                # indegree[nextCourse] -= 1
                # dfs(nextCourse, visited)
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        # for i in start:
        #     dfs(i, set())
        # # print(indegree)
        # for i in indegree:
        #     if i != 0:
        #         return False
        return output
