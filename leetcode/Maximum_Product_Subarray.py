'''
152. Maximum Product Subarray Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.top_down(nums)
    
    def top_down(self, nums: List[int]) -> int:
        
        pre_min = pre_max = glo_max = nums[0] 
        for num in nums[1:]:
            curr_min = min(num, num*pre_max, num*pre_min)
            curr_max = max(num, num*pre_max, num*pre_min)  
            glo_max = max(curr_max, glo_max)
            
            pre_min = curr_min
            pre_max = curr_max
        return glo_max
