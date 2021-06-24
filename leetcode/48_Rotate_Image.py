'''
48. Rotate Image Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflex(matrix)
        
        
    def transpose(self, matrix):
        # Since matrix size nxn
        m_len = len(matrix)
        
        for r in range(m_len):
            for c in range(r, m_len):
                matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
                
    # Reflex matrix by middle vertical axis             
    def reflex(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix)//2):
                matrix[r][c], matrix[r][len(matrix)-1-c] = matrix[r][len(matrix)-1-c], matrix[r][c]
