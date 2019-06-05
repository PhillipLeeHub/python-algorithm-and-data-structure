# 463. Island Perimeter Easy
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#
#
# Example:
#
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# https://leetcode.com/problems/island-perimeter/
def islandPerimeter(self, grid: List[List[int]]) -> int:
    '''
    Runtime: 248 ms, faster than 53.89% of Python3 online submissions for Island Perimeter.
    Memory Usage: 13.6 MB, less than 22.38% of Python3 online submissions for Island Perimeter.
    '''
    edge_count = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[0])):
            if grid[j][i] == 1:
                if i == 0:
                    edge_count += 1
                if i == len(grid[0]) - 1:
                    edge_count += 1

                if j == 0:
                    edge_count += 1
                if j == len(grid) - 1:
                    edge_count += 1

                if 0 <= i <= len(grid[0]) - 2:
                    if grid[j][i + 1] == 0:
                        edge_count += 1

                if 1 <= i <= len(grid[0]) - 1:
                    if grid[j][i - 1] == 0:
                        edge_count += 1

                if 0 <= j <= len(grid) - 2:
                    if grid[j + 1][i] == 0:
                        edge_count += 1

                if 1 <= j <= len(grid) - 1:
                    if grid[j - 1][i] == 0:
                        edge_count += 1
    return edge_count
