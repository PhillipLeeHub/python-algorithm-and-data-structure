'''
227. Basic Calculator II
Medium

1387

239

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = None
        num = 0
        s+='+' # Ensure last char is accounted for
        
        for c in s.replace(" ", ""):
            if c.isdigit():
                # Account for more than a single digit
                num = num * 10 + int(c)
                
            else:
                if operator == '/':
                    val = stack.pop()
                    #print("@@@: ", int(val/num))
                    stack.append(int(val / int(num)))
                elif operator == '*':
                    stack.append(stack.pop() * int(num))
                elif operator == '+':
                    stack.append(int(num))
                elif operator == '-':
                    stack.append(-int(num))
                else:
                    stack.append(num)
                # Saves the previous operator
                operator = c
                
                # Reset num
                num = 0
        return sum(stack)
