# 1. Two Sum Easy
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        '''
        Runtime: 36 ms, faster than 92.32% of Python3 online submissions for Two Sum.
        Memory Usage: 14.5 MB, less than 23.27% of Python3 online submissions for Two Sum.

        target = 9
        [2, 7, 11, 15]

        {
            '7':0
        }

        '''
        for index, num in enumerate(nums):
            if num in difference:
                prev_index = difference[num]
                return [prev_index, index]
            else:
                diff = target - num
                difference[diff] = (index)
