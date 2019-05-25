# 67. Add Binary Easy
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
def addBinary(self, a: str, b: str) -> str:
    # Convert "11" to integer
    a_bin = int(a, base=2)
    # Convert "1" to integer
    b_bin = int(b, base=2)

    # Add 3 + 1
    sum_bin = a_bin + b_bin

    # Format int 4 into binary string "100"
    return "{0:b}".format(sum_bin)
