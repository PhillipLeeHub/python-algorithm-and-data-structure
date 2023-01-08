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
    
    
    
    
    def reverseList_2023_attempted(self, curr_node: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 -> 2 -> 3 -> 4 -> 5 

        1 <- 2 -> 3 -> 4 -> 5
        tmp1 = 1.next
        tmp2 = 2.next 
        1 <- 2.next 

        1 <- 2 <- 3 -> 4 -> 5 
        2 <- tmp
        '''
        prev_node = None
        tail = None
        while(curr_node):
            # Save tmp variables 
            tmp_curr_node = curr_node
            tmp_next_node = curr_node.next
            
            # Reverse the linklist
            curr_node.next = prev_node

            # Set up next node
            # Save the tail
            prev_node = tmp_curr_node
            tail = tmp_curr_node
            curr_node = tmp_next_node
        return tail
        
            
            
