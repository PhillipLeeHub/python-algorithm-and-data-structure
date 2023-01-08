'''
876. Middle of the Linked List Easy
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Loop through all nodes
        Save to map with 
            {
                index: node_addr
            }
        find mid node = total number of nodes/2, round up
        return mid node
        '''
        node = head
        node_map = {}
        index = 0
        while(node):
            node_map[index] = node
            node = node.next
            index+=1
        mid_node = math.floor(index/2)

        return node_map[mid_node]
