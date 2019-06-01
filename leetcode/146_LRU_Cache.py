# 146. LRU Cache Hard
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
class Node:
    def __init__(self, num=0):
        self.num = num
        self.next = None
        self.prev = None
        self.key = None


class LRUCache:
    '''
    Runtime: 152 ms, faster than 33.05% of Python3 online submissions for LRU Cache.
    Memory Usage: 22.1 MB, less than 23.68% of Python3 online submissions for LRU Cache.
    '''

    def __init__(self, capacity: int):
        self.node_map = {}
        self.capacity = capacity
        self.count = 0
        self.tail = Node()
        self.tail.key = 'tail'

        self.head = Node()
        self.head.key = 'head'
        self.head.next = self.tail
        self.tail.prev = self.head

    def unlink_node(self, node):
        ''' remove node's next and prev links
            links prev and next nodes together
        '''
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert_to_head(self, node):
        next = self.head.next
        next.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = next

    def remove_last(self):
        last = self.tail.prev
        second_last = last.prev
        second_last.next = self.tail
        self.tail.prev = second_last
        return last.key

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]

            # Remove node from current location
            self.unlink_node(node)
            self.insert_to_head(node)

            # Add to head
            return node.num
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.num = value
            # Remove node from current location
            self.unlink_node(node)

        else:
            node = Node(value)
            node.key = key
            self.node_map[key] = node
            self.count += 1
            if self.head.next == None:
                node.prev = self.head
                self.head.next = node
            if self.tail.prev == None:
                node.next = self.tail
                self.tail.prev = node

        self.insert_to_head(node)

        if self.count > self.capacity:
            # Max cap, remove last node
            key = self.remove_last()
            del self.node_map[key]
            self.count -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)