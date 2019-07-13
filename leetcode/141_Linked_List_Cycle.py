# 141. Linked List Cycle Easy
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import Queue

def hasCycle(self, head):
    return self.iterative(head)

def iterative(self, head):
    '''
    Runtime: 116 ms, faster than 5.59% of Python online submissions for Linked List Cycle.
    Memory Usage: 19 MB, less than 5.33% of Python online submissions for Linked List Cycle.
    '''
    # Edge case, empty linked list
    if not head:
        return False

    q = Queue.Queue()
    q.put(head)
    visited_dict = {}

    while (not q.empty()):
        node = q.get()

        # Check if node has been visited
        if node in visited_dict:
            # Visited node, there is a cycle
            return True
        else:
            visited_dict[node] = 1

        # Add next node if exist
        if node.next:
            q.put(node.next)

    return False 

