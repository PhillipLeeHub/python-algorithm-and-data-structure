'''
102. Binary Tree Level Order Traversal Medium
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.dict = {}
        self.ans = []
        self.DFS(root, 0)
        
        for h in range(0, len(self.dict)):
            self.ans.append(self.dict[h])
        return self.ans
    
    def DFS(self, node, height):
        # Traverse all nodes via BFS
        # Track height
        # Resort into list
        if not node:
            return 
        
        if height in self.dict:
            self.dict[height].append(node.val)
        else:
            self.dict[height] = [node.val]
        
        self.DFS(node.left, height+1)
        self.DFS(node.right, height+1)
                
        
        
        
