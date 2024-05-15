from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def addOneRow(self, root, val, depth):
        
        # If depth = 1
        if depth == 1: 
            node = TreeNode(val)
            node.left = root
            return node
        
        # To keep track of the depth
        currDepth = 0
        
        # Queue, initialy with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # Update the depth
            currDepth += 1
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If this node is at a depth "depth - 1"
                if currDepth == depth - 1:
                    
                    prevLeft, prevRight = node.left, node.right
                    node.left = TreeNode(val)
                    node.right = TreeNode(val)
                    
                    node.left.left = prevLeft
                    node.right.right = prevRight
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
                
            # If we have added the required row, we can break
            if currDepth == depth - 1: break
        
        # Return the root node after adding the row
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

val = 1
depth = 2

print("Output -> ", Solution().addOneRow(root, val, depth))