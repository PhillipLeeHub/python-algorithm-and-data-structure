'''
763. Partition Labels Medium
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        Figure out the rightmost index first and use it to denote the start of the next section.
        
        Reset the left pointer at the start of each new section.

        Store the difference of right and left pointers + 1 as in the result for each section.      
        
        { letter : right_most_index }
        {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        
        "a b a b c b a c a   d e  f  e  g  d  e    h  i  j  h  k  l  i  j"
         0 1 2 3 4 5 6 7 8   9 10 11 12 13 14 15   16 17 18 19 20 21 22 23
        
        '''
        index_dict = {}
        count = 0
        results = []
        # Most right index for each letter
        # "ababcbaca efegde ijhklij"        
        for i, c in enumerate(S):
            index_dict[c] = i
        
        # Set up sliding window with left and right at 0
        right, left = 0, 0
        
        # Loop through all letters
        for i, c in enumerate(S):
            # Find right most value
            right = max(right, index_dict[c])
            
            # Check if we reach max right for this letter
            if i == right:
                count = right - left + 1
                results.append(count)
                left = right + 1
                
        return results    
