# 783. Minimum Distance Between BST Nodes easy
# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.
def minDiffInBST(self, root: TreeNode) -> int:
    # Iterative
    return self.iterative(root)

    # recursive
    # self.res = float('inf')
    # self.prev = -float('inf')
    # return self.recursive(root)


def iterative(self, root) -> int:
    '''
    52ms
    13MB
    '''
    self.stack = []
    self.res = float('inf')
    self.prev = -float('inf')

    curr = root
    while (len(self.stack) != 0 or curr != None):
        while (curr != None):
            self.stack.append(curr)
            curr = curr.left

        curr = self.stack.pop()
        if self.prev:
            self.res = min(self.res, curr.val - self.prev)
        self.prev = curr.val

        curr = curr.right

    return self.res


def recursive(self, root) -> int:
    '''
    40ms
    13.3MB
    '''
    if root == None:
        return None

    self.recursive(root.left)

    self.res = min(self.res, root.val - self.prev)
    self.prev = root.val

    self.recursive(root.right)
    return self.res