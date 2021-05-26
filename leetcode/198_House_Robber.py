'''
198. House Robber Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        #return self.bot_up(nums)
        self.memo = {}
        return self.top_down(nums, len(nums)-1)
    
    def top_down(self, nums: List, i) -> int:
        if i == 0:
            return nums[0]
        
        if i == 1:
            return max(nums[0], nums[1])
        
        if i in self.memo:
            return self.memo[i]

        self.memo[i] = max(self.top_down(nums, i-2) + nums[i], self.top_down(nums, i-1))
        return self.memo[i]
        
    def bot_up(self, nums: List) -> int:
        ans = [0] * len(nums) 
        
        if len(nums) == 1:
            return nums[0]
        
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # Select from current and 2 previouis
            # Or Select from 1 previous result
            ans[i] = max(ans[i-2] + nums[i], ans[i-1])
        return ans[len(nums)-1]
