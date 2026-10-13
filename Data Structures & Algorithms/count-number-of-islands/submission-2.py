class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        #path = set()
        noOfIslands = 0
        def dfs(r,c):

            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "0":
                return False

            #path.add((r,c))
            grid[r][c] = "0"
            dfs(r+1,c) 
            dfs(r-1,c)
            dfs(r,c+1) 
            dfs(r,c-1)
            #path.remove((r,c))
            #return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    noOfIslands += 1
                    dfs(r, c)  # Sink the entire connected island
        return noOfIslands


        