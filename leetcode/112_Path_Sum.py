# 112. Path Sum easy
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root == None: return False
    # return self.recursive(root, sum)
    return self.iterative(root, sum)

def recursive(self, root: TreeNode, sum: int, running_sum=0) -> bool:
    if root == None:
        return False

    running_sum += root.val
    if root.left == None and root.right == None:
        if running_sum == sum:
            return True

    return self.recursive(root.left, sum, running_sum) or self.recursive(root.right, sum, running_sum)

def iterative(self, root: TreeNode, sum: int) -> bool:
    stack = [(root, 0)]

    while (len(stack) != 0):
        node, running_sum = stack.pop()
        new_sum = node.val + running_sum
        if node.left == None and node.right == None:
            if new_sum == sum:
                return True

        if node.left: stack.append((node.left, new_sum))
        if node.right: stack.append((node.right, new_sum))

    return False