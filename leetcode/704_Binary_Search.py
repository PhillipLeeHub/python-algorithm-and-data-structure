'''
704. Binary Search Easy

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #return self.binarySearchIterative(nums, target)
        return self.binarySearchRecursive(nums, target, 0, len(nums)-1)
    
    def binarySearchIterative(self, nums: List[int], target: int) -> int:        
        l, r = 0, len(nums)-1
        
        while(l<=r):
            mid = l + (r-l)//2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
                
        return -1
    
    def binarySearchRecursive(self, nums, target, l, r) -> int:
        if l<=r:
            mid = l + (r-l)//2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return self.binarySearchRecursive(nums, target, l,  mid-1)
            else:
                return self.binarySearchRecursive(nums, target, mid+1,  r)
        else:
            return -1
