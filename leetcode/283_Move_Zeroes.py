# 283. Move Zeroes Easy
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
def moveZeroes(self, nums: List[int]) -> None:
    # self.initial_attempt(nums)
    self.optimal(nums)


def optimal(self, nums):
    '''
    [0,1,0,3,12]

zero  ^
  i  ^
    [1,3,12,0,0]
    '''
    # records the last position of "0"
    last_zero_place = 0

    # Loop through list
    for i in range(len(nums)):
        # Check non zero
        if nums[i] != 0:
            # Perform swap
            nums[i], nums[last_zero_place] = nums[last_zero_place], nums[i]

            # Advance zero
            last_zero_place += 1


def initial_attempt(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    '''
    [0,1,0,3,12]                
  z           ^
    [1,3,12,0,0]
     z   

    '''
    # Start at end of array
    # Use two pointer approach
    z = len(nums) - 2

    # While not start of aray
    while (z >= 0):
        # Swap if curr is 0, prev not 0
        if nums[z] == 0 and nums[z + 1] != 0:
            # Swap them
            nums[z], nums[z + 1] = nums[z + 1], nums[z]

            # Ensure z index within range
            if z < len(nums) - 2:
                # Move z pointer up, bubbling the zero to right
                z += 1
                # No zero to move
        else:
            # Continue down the list
            z -= 1
