# 94. Binary Tree Inorder Traversal (Medium)
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal_recursive(self, root: TreeNode) -> List[int]:
    '''
    52ms
    13.2MB
    '''
    if root == None:
        return

    self.recursive(root.left)
    self.list.append(root.val)
    self.recursive(root.right)
    return


def inorderTraversal_iterative(self, root: TreeNode) -> List[int]:
    '''
    36ms
    13.1MB
    '''
    stack = []
    list_result = []
    curr = root

    while (len(stack) != 0 or curr != None):
        while (curr != None):
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        list_result.append(curr.val)
        curr = curr.right

    return list_result