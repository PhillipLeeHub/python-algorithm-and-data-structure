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
    node = root
    # Keep traversing while stack not empty or node defined
    while (stack or node):
        # Keep going while node defined
        while (node):
            # Append all found left nodes
            stack.append(node)

            # Move to next left node
            node = node.left
        # Get node
        node = stack.pop()

        # Append to result list
        list_result.append(node.val)

        # Add right node
        node = node.right

    return list_result

def iterative(self, root):
    stack = [(root, False)]
    while(stack):
        node, visited = stack.pop()

        if node:
            if visited:
                self.ans.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
