'''
692. Top K Frequent Words Medium
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #return self.sortTwice(words, k)
        #return self.sortLambda(words, k)
        return self.sortHeap(words, k)

    def sortHeap(self, words: List[str], k: int) -> List[str]:
        import heapq
        seenDict = {}
        res_list = []
        # Loop through all words
        for word in words:
            if word in seenDict:
                seenDict[word]+=1
            else:
                seenDict[word]=1
                
        for key in seenDict:
            heapq.heappush(res_list,(-seenDict[key], key))
        
        return [heapq.heappop(res_list)[1] for _ in range(k)]
        
    def sortLambda(self, words: List[str], k: int) -> List[str]:
        seenDict = {}
        # Loop through all words
        for word in words:
            if word in seenDict:
                seenDict[word]+=1
            else:
                seenDict[word]=1
      
        '''
        Use lambda to sort the dictionary in desc order based 
        on words frequency and if frequency are equal then sort 
        dictionary in asc order based on the word alphabet.
        seenDict = {'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1}
        '''
        return sorted(seenDict, key=lambda x: (-seenDict[x], x))[:k]
    
    def sortTwice(self, words: List[str], k: int) -> List[str]:
        seenDict = {}
        # Loop through all words
        for word in words:
            if word in seenDict:
                seenDict[word]+=1
            else:
                seenDict[word]=1
        
        # Convert Dict to List
        wordList = [[letter, count] for letter, count in seenDict.items()]
        
        # Sort by word by lower to higher
        wordList.sort(key=lambda x: x[0])
        
        # Sort by count by highest to lowest
        wordList.sort(key=lambda x: x[1], reverse=True)
        
        # Sort the array with most occurances, followed by lower alphabet
        return [x[0] for x in wordList][:k]
        
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
#Solution().topKFrequent(words, k)        


                
