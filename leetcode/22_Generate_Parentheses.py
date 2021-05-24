'''
22. Generate Parentheses Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack(n)
        return self.ans
        
    def backtrack(self, n: int, stack=[], left=0, right=0):
        if len(stack) == n*2:
            self.ans.append(''.join(stack))
            
        if (left < n):
            stack.append('(')
            self.backtrack(n, stack, left+1, right)
            stack.pop()
            
        if (left > right):
            stack.append(')')
            self.backtrack(n, stack, left, right+1)
            # Pop to back track
            stack.pop()
            
