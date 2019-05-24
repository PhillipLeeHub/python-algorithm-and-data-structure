# 24. Swap Nodes in Pairs Medium
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
def swapPairs(self, head: ListNode) -> ListNode:
    return self.recurive(head)
    # return self.iterative(head)


def recurive(self, head: ListNode) -> ListNode:
    '''
    Runtime: 36 ms, faster than 88.34% of Python3 online submissions for Swap Nodes in Pairs.
    Memory Usage: 13.1 MB, less than 50.90% of Python3 online submissions for Swap Nodes in Pairs.
    '''
    if head == None:
        return head

    if head.next == None:
        return head

    node_1 = head
    node_2 = head.next
    node_1.next, node_2.next = node_2.next, node_1
    node_1.next = self.recurive(node_1.next)
    return node_2


def iterative(self, head: ListNode) -> ListNode:
    '''
    Runtime: 28 ms, faster than 99.69% of Python3 online submissions for Swap Nodes in Pairs.
    Memory Usage: 13.1 MB, less than 58.07% of Python3 online submissions for Swap Nodes in Pairs.
    '''
    dummy_head = ListNode(0)
    curr_node = dummy_head
    curr_node.next = head

    while (curr_node.next != None and curr_node.next.next != None):
        node_1 = curr_node.next
        node_2 = curr_node.next.next
        curr_node.next = node_2
        node_1.next, node_2.next = node_2.next, node_1

        curr_node = node_1

    return dummy_head.next

