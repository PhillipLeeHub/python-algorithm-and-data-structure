# 59. Spiral Matrix II Medium
# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
def generateMatrix(self, n: int) -> List[List[int]]:
    '''
    Runtime: 36 ms, faster than 93.35% of Python3 online submissions for Spiral Matrix II.
    Memory Usage: 13.1 MB, less than 66.75% of Python3 online submissions for Spiral Matrix II.
    '''

    arr_out = [[0] * n for i in range(n)]

    top = 0
    left = 0
    bottom = n - 1
    right = n - 1
    count = 1
    j = 0
    i = 0

    while (left <= right and top <= bottom):

        for i in range(left, right + 1, 1):
            arr_out[top][i] = count
            count += 1
        top += 1

        for j in range(top, bottom + 1, 1):
            arr_out[j][right] = count
            count += 1
        right -= 1

        for i in range(right, left - 1, -1):
            arr_out[bottom][i] = count
            count += 1
        bottom -= 1

        for j in range(bottom, top - 1, -1):
            arr_out[j][left] = count
            count += 1
        left += 1
    for x in arr_out:
        print(x)
    return arr_out