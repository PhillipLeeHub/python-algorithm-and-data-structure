'''
200. Number of Islands Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(i,j, grid)
                    island_count+=1
        return island_count

    # Change island to water via DFS
    def DFS(self, i, j, grid):
        stack = [(i, j)]
        
        while(len(stack) !=0):
            i,j = stack.pop()
            
            # Set to 0
            grid[i][j] = '0'
            
            for _i, _j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                cell_i = i + _i
                cell_j = j + _j
                if 0 <= cell_i < len(grid) and 0 <= cell_j < len(grid):
                    if grid[cell_i][cell_j] == '1':
                        stack.append((cell_i,cell_j))
                        
         
        
        
