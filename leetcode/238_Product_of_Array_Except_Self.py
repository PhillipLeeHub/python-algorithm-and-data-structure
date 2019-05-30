# 238. Product of Array Except Self Medium
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # return self.cross_multiple_v1(nums)
    return self.cross_multiple_v2(nums)


def cross_multiple_v2(self, nums: List[int]) -> List[int]:
    '''
    Runtime: 100 ms, faster than 91.20% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 20.8 MB, less than 9.47% of Python3 online submissions for Product of Array Except Self.
    '''
    arr_out = [1] * len(nums)
    i = 1
    j = len(nums) - 2
    product_A = 1
    product_B = 1
    while (i < len(nums)):
        product_A *= nums[i - 1]
        product_B *= nums[j + 1]
        arr_out[i] *= product_A
        arr_out[j] *= product_B

        i += 1
        j -= 1
    return arr_out

    # [1,2,3,4]
    # [1,1,2,1]
    # A = 2
    # B = 1


def cross_multiple_v1(self, nums: List[int]) -> List[int]:
    '''
    Runtime: 140 ms, faster than 6.36% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 20.5 MB, less than 73.21% of Python3 online submissions for Product of Array Except Self.
    '''
    arr_a = []
    arr_b = []
    arr_out = []
    #   [1,  2,  3, 4]
    #   [1,  1,  2, 6] Cross multiple
    #   [24, 12, 4, 1]

    running_product = 1
    i = 0
    while (i < len(nums)):
        arr_a.append(running_product)
        running_product *= nums[i]
        i += 1

    running_product = 1
    i = len(nums) - 1
    while (i >= 0):
        arr_b.append(running_product)
        running_product *= nums[i]
        i -= 1
    # print(arr_b)

    # Multiple both list
    i = 0
    while (i < len(nums)):
        arr_out.append(arr_a[i] * arr_b[len(nums) - 1 - i])
        i += 1
    return arr_out



