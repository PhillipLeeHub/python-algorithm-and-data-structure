'''
206. Reverse Linked List Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #return self.iterative(head);
        return self.recursive(head);

    
    
    def iterative(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while(curr): 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def recursive(self, curr, prev=None) -> ListNode:
        if not curr:
            return prev
        tmp_next = curr.next
        curr.next = prev
        prev = curr
        curr = tmp_next
        
        return self.recursive(curr, prev)
        
            
            
