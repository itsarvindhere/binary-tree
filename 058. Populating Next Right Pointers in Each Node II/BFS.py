from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        
        # Queue, initially with the root node
        queue = deque()
        if root: queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # Count of nodes in the current level
            nodesInCurrentLevel = len(queue)
            
            # Previous node in current level
            prev = None
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Update the next pointer of the previous node in this level, if it exists
                if prev: prev.next = node
                
                # Update the prev node
                prev = node
                
                # If the node has a left child, push to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push to the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
        # Finally, return the tree
        return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

print("Output -> ", Solution().connect(root))