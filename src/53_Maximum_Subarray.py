# 53. Maximum Subarray easy
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
def maxSubArray(self, nums: List[int]) -> int:
    # return self.brude_force(nums)
    return self.dp(nums)


def dp(self, nums: List[int]) -> int:
    total_max = nums[0]
    total = 0
    for i in range(0, len(nums)):
        total = max(nums[i], nums[i] + total)
        total_max = max(total_max, total)

    return total_max


# Cause timeout
def brude_force(self, nums: List[int]) -> int:
    total = float('-inf')
    i = 0
    j = 0
    sizeOfList = len(nums)

    if sizeOfList == 1:
        return nums[0]

    while (i <= sizeOfList):
        curr_total = float('-inf')
        j = i + 1
        while (j <= sizeOfList):
            curr_total = sum(nums[i:j])
            total = max(total, curr_total)
            j += 1
        i += 1
    return total