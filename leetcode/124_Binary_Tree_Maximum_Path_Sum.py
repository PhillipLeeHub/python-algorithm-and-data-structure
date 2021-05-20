'''
124. Binary Tree Maximum Path Sum Hard
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")
        self.find_max(root)
        return self.max_sum
        
    def find_max(self, node):
        if node == None:
            return 0 
        
        max_right_sum = max(self.find_max(node.right), 0)
        max_left_sum = max(self.find_max(node.left), 0)
        
        self.max_sum = max(node.val + max_right_sum + max_left_sum, self.max_sum)
    
        return node.val + max(max_right_sum, max_left_sum)
            
        
