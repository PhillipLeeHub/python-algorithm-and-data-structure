# 54. Spiral Matrix Medium
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    '''
    Runtime: 36 ms, faster than 85.68% of Python3 online submissions for Spiral Matrix.
    Memory Usage: 13.2 MB, less than 39.92% of Python3 online submissions for Spiral Matrix.
    '''
    if len(matrix) == 0:
        return []

    num_of_elem = len(matrix) * len(matrix[0])
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    counter = 0
    arr_out = []
    while (counter < num_of_elem):
        for i in range(left, right + 1):
            arr_out.append(matrix[top][i])
            counter += 1
        top += 1

        if counter >= num_of_elem: break

        for j in range(top, bottom + 1):
            arr_out.append(matrix[j][right])
            counter += 1
        right -= 1

        if counter >= num_of_elem: break

        for i in range(right, left - 1, -1):
            arr_out.append(matrix[bottom][i])
            counter += 1
        bottom -= 1

        if counter >= num_of_elem: break

        for j in range(bottom, top - 1, -1):
            arr_out.append(matrix[j][left])
            counter += 1
        left += 1
    return arr_out

