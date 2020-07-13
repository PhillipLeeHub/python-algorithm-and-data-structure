'''
739. Daily Temperatures Medium

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #return self.bf(T)
        return self.useStack(T)
    
    def useStack(self, T):
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            # While stack populated and
            # Current Temp greater than previous
            # Note: Keeps comparing the top of the stack to current temp.
            while stack and  T[i] > T[stack[-1]]:
                index = stack.pop()
                # Calculate the number of days
                ans[index] = i - index
            
            # Add the day index to the stack
            stack.append(i)
        
        return ans
    
    
    def bf(self, T):
        # Time limit exceeded
        ans = [0] * len(T)
        for i in range(0, len(T)):
            for j in range(i+1 , len(T)):
                if T[i] < T[j]:
                    ans[i] = j - i
                    break
        return ans
                    
            
            
            
            
        
