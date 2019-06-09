# 133. Clone Graph Medium
# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
#
#
#
# Example:
#
# https://leetcode.com/problems/clone-graph/
#
# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
#
# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.

# Note:
#
# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned graph.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
import queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #return self.bfs(node)
        #return self.dfs(node)
        visited = {}
        return self.clone_recursive(node, visited)

    def clone_recursive(self, node: 'Node', visited) -> 'Node':
        '''
        Runtime: 48 ms, faster than 50.05% of Python3 online submissions for Clone Graph.
        Memory Usage: 14.4 MB, less than 5.27% of Python3 online submissions for Clone Graph.
        '''
        visited[node] = Node(node.val, [])

        for neighbor in node.neighbors:
            if neighbor in visited:
                visited[node].neighbors.append(visited[neighbor])
            else:
                self.clone_recursive(neighbor, visited)
                visited[node].neighbors.append(visited[neighbor])

        return visited[node]


    def bfs(self, node: 'Node') -> 'Node':
        # Set up queue for edge connection
        q = queue.Queue()
        q.put(node)

        # Dictionary helps see which node has been visited
        visited = {node:Node(node.val, [])}
        while(not q.empty()):
            node = q.get()
            #print('node: ', node.val)
            # Loop through all neighbors for this node
            for neighbor in node.neighbors:
                #print('neighbor: ', neighbor.val)
                # Check if neighbor never seen
                if neighbor not in visited:
                    # Clone new neighbor
                    visited[neighbor] = Node(neighbor.val, [])

                    # Add to queue for edge connection
                    q.put(neighbor)

                # Add edge connection
                visited[node].neighbors.append(visited[neighbor])

        return visited[node]

    def dfs(self, node: 'Node') -> 'Node':
        # Set up stack for edge connection
        s = []
        s.append(node)

        # Dictionary helps see which node has been visited
        visited = {node:Node(node.val, [])}
        while(len(s) != 0):
            node = s.pop()
            #print('node: ', node.val)
            # Loop through all neighbors for this node
            for neighbor in reversed(node.neighbors):
            #for neighbor in node.neighbors:
                #print('neighbor: ', neighbor.val)
                # Check if neighbor never seen
                if neighbor not in visited:
                    # Clone new neighbor
                    visited[neighbor] = Node(neighbor.val, [])

                    # Add to queue for edge connection
                    s.append(neighbor)

                # Add edge connection
                visited[node].neighbors.append(visited[neighbor])

        return visited[node]

