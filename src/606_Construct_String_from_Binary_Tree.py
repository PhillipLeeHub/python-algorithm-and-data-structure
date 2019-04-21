# 606. Construct String from Binary Tree (Easy)
# You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
#
# The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
#
# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# Output: "1(2(4))(3)"
#
# Explanation: Originallay it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".
# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
#
# Output: "1(2()(4))(3)"
#
# Explanation: Almost the same as the first example,
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
def tree2str_recursive(self, t: TreeNode):

    if t == None:
        return

    print('t.val: ', t.val)
    self.my_str += str(t.val)

    if t.left == None and t.right:
        self.my_str += '()'
    if t.left:
        print('t.left: ', t.left.val)
        self.my_str += '('
        self.recursive(t.left)
        self.my_str += ')'

        # if t.right == None and t.left:
    #     self.my_str+='()'
    if t.right:
        print('t.right: ', t.right.val)
        self.my_str += '('
        self.recursive(t.right)
        self.my_str += ')'

def tree2str_iterative(self, t: TreeNode):
    stack = []
    result = ''
    stack.append(t)
    while (len(stack) != 0):

        curr = stack.pop()

        if curr == None:
            continue

        if curr == '(':
            result += '('
            continue

        if curr == ')':
            result += ')'
            continue

        result += str(curr.val)

        if curr.right:
            stack.append(')')
            stack.append(curr.right)
            stack.append('(')

        if curr.left == None and curr.right:
            stack.append(')')
            stack.append('(')
            continue

        if curr.left:
            stack.append(')')
            stack.append(curr.left)
            stack.append('(')
    return result