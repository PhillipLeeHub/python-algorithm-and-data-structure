'''
344. Reverse String Easy

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for index in range(len(s)//2):
            s[index],s[len(s)-1 - index] = s[len(s)-1 - index], s[index]
        
    def reverseStringMarch2021(self, s: List[str]) -> None:
     start_p = 0
        end_p = len(s)-1
        
        while (start_p < end_p):
            s[start_p], s[end_p] = s[end_p], s[start_p]
            start_p+=1
            end_p-=1
    
