# 23. Merge k Sorted Lists hard
# Hard
#
# 2414
#
# 155
#
# Favorite
#
# Share
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
def __init__(self):
    self.counter = itertools.count()


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    return self.use_priority_queue(lists)


def use_priority_queue(self, lists: List[ListNode]) -> ListNode:
    '''
    Runtime: 164 ms, faster than 26.43% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 16.9 MB, less than 32.59% of Python3 online submissions for Merge k Sorted Lists.
    '''

    # Create priority queue
    q = PriorityQueue()

    # Create head of link list
    head = ListNode(0)
    curr_node = head

    # Loop through all the list
    # Put the first linked list in Priority Queue
    for link in lists:
        # ensure link list defined
        if link:
            # Add to queue
            # In python 3 to avoid duplicate elements in tuple caused comparison
            # failure like "TypeError: '<' not supported between instances of
            # 'ListNode' and 'ListNode'", use a unique id as the second element
            # in the tuple.
            q.put((link.val, next(self.counter), link))

    # While we go over all linked list
    while (not q.empty()):
        _, count, node = q.get()
        curr_node.next = node

        if node.next:
            q.put((node.next.val, next(self.counter), node.next))

        curr_node = node
    return head.next



