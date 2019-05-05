# 76. Minimum Window Substring hard
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #return self.brude_force(s,t)
        return self.sliding_window(s,t)
    
    def sliding_window(self, s: str, t: str) -> str:
        self.dict = {}
        self.dict_valid_count =0
        self.t = t
        self.result = ''
        self.min_result = None
        for char in t:
            self.dict[char] = 0
            
        L = 0
        R = 0
        while(R < len(s) or L< len(s)):
            # print('dict: ', self.dict)
            if not self.isValid() and R < len(s):
                #print('add',s[R] )
                self.add_char(s[R])
                R +=1
            else:
                #print('remove',s[L] )
                self.remove_char(s[L])
                L +=1
            
            #print(self.result)
        if self.min_result == None:
            return ""
        return self.min_result
    
    
    def add_char(self, char):
        self.result += char
        if char in self.dict:
            if self.dict[char] == 0:
                self.dict_valid_count+=1
            self.dict[char] += 1
            
    def remove_char(self, char):
        self.result = self.result[1:]
        if char in self.dict:
            self.dict[char] -= 1
            if self.dict[char]==0:
                self.dict_valid_count-=1
            
    def isValid(self):
        print('self.dict_valid_count: ',self.dict_valid_count)
        if len(self.t) == self.dict_valid_count:
            if self.min_result == None:
                self.min_result = self.result 
            elif len(self.result)<len(self.min_result):
                self.min_result = self.result 
            return True
        return False
    
    
    # TIME OUT EXCEEL
    def brude_force(self, s: str, t: str) -> str:
        min_result = ''
        isMatch = False
        for i, char in enumerate(s):
            result = ''
            isMatch = False
            T_copy = list(t) 
            if char not in T_copy:
                continue                
            for i ,c in enumerate(s[i:]):                
                result += c
                if c in T_copy:
                    T_copy.remove(c)
                if (len(T_copy) == 0):
                    isMatch = True
                    break
            
            if isMatch:
                if min_result == "":
                    min_result = result
                elif len(result) < len(min_result):
                    min_result = result   
        if len(min_result)==0:
            return ""
        return min_result
    
                    
                
                    
                
