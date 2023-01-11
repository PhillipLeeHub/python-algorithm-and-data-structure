'''
409. Longest Palindrome Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = {}
        pair_count = 0
        isOdd = False
        for c in s:
            if c in count_map:
                count_map[c]+=1
            else:
                count_map[c]=1
        
        for key, value in count_map.items():
            pair_count+=value//2
            if value%2:
                isOdd = True
        
        # Check for odd digit for center
        if isOdd:
            extra_c = 1
        else:
            extra_c = 0

        return pair_count*2 + extra_c
