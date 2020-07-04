'''
21. Merge Two Sorted Lists Easy

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #return self.iterative(l1, l2)
        return self.recursive(l1, l2)

    def iterative(self, l1, l2):
        head = ListNode()
        curr = head
        
        while(l1 or l2):
            if not l1:
                curr.next = l2
                break 
                
            if not l2:
                curr.next = l1 
                break
                
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        return head.next
    
    def recursive(self, l1, l2):
        head = ListNode()
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        curr = None
        if l1.val < l2.val:
            curr = l1
            curr.next = self.recursive(l1.next, l2)
        else:
            curr = l2
            curr.next = self.recursive(l1, l2.next)
        
        return curr
        
