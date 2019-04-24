# 560. Subarray Sum Equals K medium
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
def subarraySum(self, nums: List[int], k: int) -> int:
    return self.dp(nums, k)


def dp(self, nums: List[int], k: int) -> int:
    '''
    Runtime: 60 ms, faster than 73.67% of Python3 online submissions for Subarray Sum Equals K.
    Memory Usage: 15.4 MB, less than 11.54% of Python3 online submissions for Subarray Sum Equals K.
    '''
    pre_sums = {0: 1}
    sum = 0
    counter = 0

    for num in nums:
        sum += num
        # print('sum: ',sum)
        # print(pre_sums)
        counter += pre_sums.get(sum - k, 0)

        if pre_sums.get(sum):
            pre_sums[sum] += 1
        else:
            pre_sums[sum] = 1
    return counter


# TIME LIMIT EXCEEDED
def bruce_force(self, nums: List[int], k: int) -> int:
    result = 0
    start = 0
    while (start <= len(nums) - 1):
        end = start
        total = 0
        while (end <= len(nums) - 1):
            total = nums[end] + total
            if total == k:
                result += 1
            # print(start, end, total)
            end += 1
        start += 1
    return result
