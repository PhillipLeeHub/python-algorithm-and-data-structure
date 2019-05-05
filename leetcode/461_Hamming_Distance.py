# 461. Hamming Distance easy 
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xor = x^y
        bin_str = "{0:032b}".format(xor)
        print(bin_str)
        count =0
        for char in bin_str:
            if char == '1':
                count +=1
        return count
