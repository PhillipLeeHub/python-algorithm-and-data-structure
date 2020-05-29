'''
    347. Top K Frequent Elements Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.heap(nums, k)
    
    def heap(self, nums: List[int], k: int) -> List[int]:
        res_list = []
        seen_dict = {}
        
        # Loop through all nums and count them
        # Note: Negative counting due to heappop() gives min
        for num in nums:
            if num in seen_dict:
                seen_dict[num]-=1
            else:
                seen_dict[num]=-1
        
        # Push count tuple into heap
        for num, count in seen_dict.items():
           heapq.heappush(res_list, (count, num))
        
        # return the number k nums
        return [heapq.heappop(res_list)[1] for _ in range(k)]
