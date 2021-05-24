'''
78. Subsets Medium
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.iterative(nums)
        results = []
        self.recursive(nums, [], results)
        return results
        
    def recursive(self, nums, curr_list, results):
            
        results.append(curr_list)
        for i, num in enumerate(nums):
            self.recursive(nums[i+1:], curr_list+[num], results)
                
    
    def iterative(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        # Iterate through all numbers
        for i, num in enumerate(nums):
            # Iterate for each current ans
            for j in range(len(ans)):
                # Create new list
                curr_list = []
                # Add the current number to each current ans in new list
                curr_list += ans[j] + [num]
                
                # Append new list to ans
                ans.append(curr_list)
        return ans
            
        
