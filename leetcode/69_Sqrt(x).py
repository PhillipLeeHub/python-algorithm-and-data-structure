# 69. Sqrt(x) Easy
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
def mySqrt(self, x: int) -> int:
    '''
    Runtime: 56 ms, faster than 54.11% of Python3 online submissions for Sqrt(x).
    Memory Usage: 13.1 MB, less than 79.16% of Python3 online submissions for Sqrt(x).
    '''
    # 2^2 = 4
    # 2.82842^2 = 8

    # x > 1, range(1, x)
    # x < 1, range(0, 1)
    if x == 1 or x == 0:
        return x
    max_range = max(1, x)
    min_range = 0
    result = 0
    while (max_range - min_range != 0):

        mid = min_range + (max_range - min_range) // 2
        result = mid * mid
        print(result)
        if int(result) <= x < (mid + 1) * (mid + 1):
            return int(mid)

        if result < x:
            min_range = mid
        else:
            max_range = mid
