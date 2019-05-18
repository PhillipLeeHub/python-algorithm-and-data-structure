# 11. Container With Most Water medium
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
# are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# https://leetcode.com/problems/container-with-most-water/
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
# (blue section) the container can contain is 49.
def maxArea(self, height: List[int]) -> int:
    return self.two_pointer(height)

def two_pointer(self, height: List[int]) -> int:
    L = 0
    R = len(height) - 1
    max_area = float('-inf')
    while (L < R):
        min_height = min(height[L], height[R])
        area = min_height * (R - L)
        max_area = max(area, max_area)

        if height[L] >= height[R]:
            R -= 1
        else:
            L += 1
    return max_area


# Time Limit Exceeded
def bf(self, height: List[int]) -> int:
    maxed_area = float('-inf')
    max_cord = 0
    for i in range(0, len(height) - 1):
        for j in range(i + 1, len(height)):
            min_height = min(height[i], height[j])
            curr_area = abs(j - i) * min_height
            if curr_area > maxed_area:
                max_cord = (j, i)
                maxed_area = curr_area
    print(max_cord)
    return maxed_area