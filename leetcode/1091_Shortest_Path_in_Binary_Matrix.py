'''
1091. Shortest Path in Binary Matrix Medium

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1. 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''
from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        perform BFS 
        8 directions 
        get shortest path...
        
        [[0,0,0,0,1],
         [1,0,0,0,0],
         [0,1,0,1,0],
         [0,0,0,1,1],
         [0,0,0,1,0]]
        '''
        r_size = len(grid)
        c_size = len(grid[0])
        
        # Check for edge cases
        if grid[0][0] or grid[r_size-1][c_size-1]:
            return -1
        
        visited = {}
        q = Queue()
        # Put starting point
        q.put((0,0,1))
        
        # Loop while queue not empty
        while(not q.empty()):            
            r, c, path_count = q.get()
            
            # Check if end location
            if r == len(grid)-1 and  c == len(grid[0])-1:
                return path_count
                    
            # Loop through 8 directions
            for _r, _c in [(-1,-1), (0,-1),(1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]:
                # Test each direction
                curr_r, curr_c = r+_r, c+_c
                
                # Ensure within grid range
                if 0 <= curr_r < len(grid) and 0 <= curr_c < len(grid[0]):
                    # Check if cell has been visited
                    if (curr_r, curr_c) in visited:
                        continue
                    else:
                        visited[(curr_r, curr_c)] = 1
                    
                    # If path is available
                    if grid[curr_r][curr_c] == 0:
                        # Add new path to queue
                        q.put((curr_r, curr_c, path_count+1))
                        
        # No paths found, return -1                    
        return -1
    
