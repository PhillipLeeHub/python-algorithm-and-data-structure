'''
506. Relative Ranks Easy

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        medals = ["Bronze Medal", "Silver Medal", "Gold Medal"]
        index_dict = {}
        res_arr = [None] * len(nums)

        for index, num in enumerate(nums):
            index_dict[num] = index

        sorted_nums = sorted(nums, reverse=True)
        
        
        
        for _index, _num in enumerate(sorted_nums):
            num_index = index_dict[_num]
            if len(medals) > 0:                
                res_arr[num_index] = medals.pop()
            else:
                res_arr[num_index] = str(_index+1)
   
            
        return res_arr
            
                
        
