# 118. Pascal's Triangle easy
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
def generate(self, numRows: int) -> List[List[int]]:
    '''
    Runtime: 28 ms, faster than 99.36% of Python3 online submissions for Pascal's Triangle.
    Memory Usage: 13.3 MB, less than 13.67% of Python3 online submissions for Pascal's Triangle.
    '''
    arr_out = [[1], [1, 1]]
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return arr_out

    for i in range(2, numRows):
        arr_curr = [0] * (i + 1)
        arr_curr[0] = 1
        arr_curr[len(arr_curr) - 1] = 1
        for j in range(1, len(arr_curr) - 1):
            arr_curr[j] = arr_out[i - 1][j] + arr_out[i - 1][j - 1]
        # print(arr_curr)
        arr_out.append(arr_curr)
    return arr_out
