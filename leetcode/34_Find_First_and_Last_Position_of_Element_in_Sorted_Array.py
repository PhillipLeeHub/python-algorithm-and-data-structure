'''
34. Find First and Last Position of Element in Sorted Array Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        results = [-1, -1]
        results[0] = self.findLow(nums, target)
        results[1] = self.findHigh(nums, target)
        return results

    def findLow(self, nums, target):
        l = 0
        r = len(nums) - 1
        index = -1
        while(l<=r):
      
            mid = l + (r-l)//2
            if nums[mid] == target:
                index = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return index
    
    def findHigh(self, nums, target):
        l = 0
        r = len(nums) - 1
        index = -1
        while(l<=r):
            mid = l + (r-l)//2
            if nums[mid] == target:
                index = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return index

