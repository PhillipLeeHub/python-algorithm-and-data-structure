'''
215. Kth Largest Element in an Array Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return self.sorted(nums, k)
        return self.use_heap(nums, k)
    
    def use_heap(self, nums, k):
        import heapq
        h = []
        for num in nums:
            heapq.heappush(h, num)
        
        return heapq.nlargest(k, h, key=None)[k-1]
        
        
        
    def sorted(self, nums, k):
        '''
        nums:   [3,2,1,5,6,4]
        Sorted: [1 2 3 4 5 6]
        Index:   0 1 2 4 5 6
        k=2
        '''
        nums.sort()
        return nums[len(nums)-k]
    
    
