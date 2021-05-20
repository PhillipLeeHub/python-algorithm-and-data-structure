'''
144. Binary Tree Preorder Traversal Easy
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [1,2]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        #self.recursive(root)
        self.iterative(root)
        return self.ans
    
    def recursive(self, node):
        if not node:
            return
        
        self.ans.append(node.val)
        self.recursive(node.left)
        self.recursive(node.right)
        
    def iterative(self, root):
        stack = [root]
        while(len(stack)>0):
            node = stack.pop()
            print(node)
            if node:
                self.ans.append(node.val)
                # Note: Right leaf first due to using a stack
                # Preorder, Root, left, right
                stack.append(node.right)
                stack.append(node.left)
