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
        result_arr = [0] * (len(nums))
        # {score:index} 
        score_dict = {}
        
        for index, num in enumerate(nums):
            score_dict[num] = index
        nums.sort(reverse=True)
        
        for index, num in enumerate(nums):
            if medals:
                result_arr[score_dict[num]] = medals.pop()
            else:
                result_arr[score_dict[num]] = str(index+1)
                
        return result_arr
                
        
