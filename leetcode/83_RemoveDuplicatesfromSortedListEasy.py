'''
83. Remove Duplicates from Sorted List Easy

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        head -> node -> node -> None
        1        1       2
        '''
        if not head:
            return None
        
        cur_node = head.next
        prev_node = head
        while(cur_node != None):
            
            if cur_node.val == prev_node.val:
                # Duplicate found
                cur_node = cur_node.next
                
            else:
                # Non duplicate, add to link list
                prev_node.next = cur_node
                
                # Reset previous node
                prev_node = cur_node
                # Reset current node
                cur_node = cur_node.next
                
        # Reach the end, reset the previous next Node to None
        prev_node.next = None
        return head
