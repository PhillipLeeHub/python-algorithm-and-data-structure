# 653. Two Sum IV - Input is a BST easy
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
# 
# Example 1:
# 
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# Target = 9
# 
# Output: True
#  
# 
# Example 2:
# 
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# Target = 28
# 
# Output: False
def findTarget(self, root: TreeNode, k: int) -> bool:
        import queue
        seen_nums = {}
        
        q = queue.Queue()
        
        q.put(root)
        
        while(not q.empty()):
            node = q.get()
            if node.val in seen_nums:
                return True
            
            else:
                seen_nums[k-node.val] = 1
            
            if node.left:
                q.put(node.left)
                
            if node.right:
                q.put(node.right)
        return False        
