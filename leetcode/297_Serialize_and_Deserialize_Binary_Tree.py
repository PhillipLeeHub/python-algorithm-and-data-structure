# 297. Serialize and Deserialize Binary Tree Hard
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Example:
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    '''
    Runtime: 276 ms, faster than 5.17% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    Memory Usage: 18.3 MB, less than 31.68% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized_string = self.serialize_tree(root)
        # print(serialized_string)
        return serialized_string

    def serialize_tree(self, root):
        if root == None:
            return '#' + ' '
        result = str(root.val) + ' '
        result += self.serialize_tree(root.left)
        result += self.serialize_tree(root.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        import queue
        data_list = data.strip().split(' ')
        # print(data_list)

        q = queue.Queue()
        for letter in data_list:
            q.put(letter)
        return self.deserialize_string(q)

    def deserialize_string(self, q):
        node = q.get()
        if node == '#':
            return None
        node = TreeNode(node)
        node.left = self.deserialize_string(q)
        node.right = self.deserialize_string(q)
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))