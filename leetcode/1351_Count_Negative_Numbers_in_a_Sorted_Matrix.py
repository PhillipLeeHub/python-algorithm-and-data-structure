'''
1351. Count Negative Numbers in a Sorted Matrix Easy

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
'''class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # binary search for -numbers for each list. Count the number of negatives

        total_neg = 0
        # Loop through each list 
        for arr in grid:
            neg_count = self.bst_neg(arr)
            total_neg+=neg_count
        return total_neg

    # returns number of negative ints
    def bst_neg(self, arr) -> int:
        l = 0
        r = len(arr) - 1
        
        neg_count = 0
        while(l<=r):
            mid = l + (r-l)//2
            
            if arr[mid] < 0:
                r = mid - 1
                neg_count = len(arr) - mid
            if arr[mid] >= 0:
                l = mid + 1
        return neg_count
                
