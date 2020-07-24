'''
240. Search a 2D Matrix II Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    
        if not len(matrix)or not len(matrix[0]):
            return False
        
        for row, arr in enumerate(matrix):
            print(arr)
            left = 0
            right = len(matrix[row])-1
            while (left<=right):
                print(left, right)
                mid = left + (right-left)//2            
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] > target:
                    right = mid - 1            
                else:
                    left = mid + 1

        return False
            
