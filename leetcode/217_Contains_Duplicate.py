# 217. Contains Duplicate Easy
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
def containsDuplicate(self, nums: List[int]) -> bool:
    '''
    Input: [1,2,3,1]
    Runtime: 44 ms, faster than 82.05% of Python3 online submissions for Contains Duplicate.
    Memory Usage: 19.6 MB, less than 21.13% of Python3 online submissions for Contains Duplicate.
    '''
    seen_dict = {}
    for num in nums:
        if num not in seen_dict:
            seen_dict[num] = 1
        else:
            return True
    return False