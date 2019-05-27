# 39. Combination Sum Medium
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    '''
    Runtime: 100 ms, faster than 49.92% of Python3 online submissions for Combination Sum.
    Memory Usage: 13.3 MB, less than 18.07% of Python3 online submissions for Combination Sum.
    '''
    result_arr = []
    curr_arr = []
    self.dfs(candidates, target, result_arr, curr_arr, 0)
    return result_arr


def dfs(self, nums, target, result_arr, curr_arr, index):
    if target < 0:
        return
    if target == 0:
        result_arr.append(curr_arr)

    for i in range(index, len(nums)):
        self.dfs(nums, target - nums[i], result_arr, curr_arr + [nums[i]], i)