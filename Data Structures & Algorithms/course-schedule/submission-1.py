class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i:[] for i in range(numCourses)}

        for crs,preq in prerequisites:
            preMap[crs].append(preq)

        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)

            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True