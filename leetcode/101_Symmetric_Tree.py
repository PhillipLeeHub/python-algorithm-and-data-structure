# 101. Symmetric Tree (Easy)
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
import queue
# def isSymmetric(self, root: TreeNode) -> bool:
#     self.queue = queue.Queue()
#     # return self.recursive(root, root)
#     return self.iterative(root)
def isSymmetric_recursive(self, root1: TreeNode, root2: TreeNode) -> bool:
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False

    if root1.val != root2.val:
        return False

    return (self.recursive(root1.left, root2.right) and
            self.recursive(root2.left, root1.right))

def isSymmetric_iterative(self, root: TreeNode) -> bool:
    result = True
    self.queue.put(root)
    self.queue.put(root)
    while (not self.queue.empty()):
        root1 = self.queue.get()
        root2 = self.queue.get()

        if root1 == None and root2 == None:
            continue

        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        self.queue.put(root1.left)
        self.queue.put(root2.right)

        self.queue.put(root2.left)
        self.queue.put(root1.right)
    return result