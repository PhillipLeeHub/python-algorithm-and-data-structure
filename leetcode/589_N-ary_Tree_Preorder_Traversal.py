// 589. N-ary Tree Preorder Traversal easy
// Given an n-ary tree, return the preorder traversal of its nodes' values.
//
// For example, given a 3-ary tree:
//
//
// Return its preorder traversal as: [1,3,5,6,2,4].

def preorder(self, root: 'Node') -> List[int]:
    self.pre_list = []
    # self.recurrsive(root)
    self.iterative(root)
    return self.pre_list

def recurrsive(self, root: 'Node') -> List[int]:
    if root == None:
        return

    self.pre_list.append(root.val)
    for i, child in enumerate(root.children):
        self.recurrsive(root.children[i])

def iterative(self, root: 'Node') -> List[int]:

    if not root:
        return
    stack = []
    stack.append(root)
    while len(stack) > 0:
        root = stack.pop()
        self.pre_list.append(root.val)
        for i, child in reversed(list(enumerate(root.children))):
            stack.append(root.chi
