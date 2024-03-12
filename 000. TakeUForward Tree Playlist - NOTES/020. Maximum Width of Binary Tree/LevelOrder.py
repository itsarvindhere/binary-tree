from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        
        # To keep the maximum width of the binary tree
        maxWidth = 1
        
        # Queue for Level Order Traversal
        queue = deque()
        
        # We will denote each node by a number, starting from "1" for the root node
        # For next level, we will go like 2 and 3... and then so on
        
        # Initially, the queue will have the root node
        queue.append([root, 1])
        
        # While the queue is not empty
        while queue:
            
            # Update the maximum width
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1)
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Go over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue, along with its number
                node, num = queue.popleft()
                
                # Push the left child to the queue, if it exists
                # If a node has a number "i", its left child will have a number "2*i"
                if node.left: queue.append([node.left, 2 * num])
                
                # Push the right child to the queue, if it exists
                # If a node has a number "i", its right child will have a number "(2*i) + 1"
                if node.right: queue.append([node.right, (2 * num) + 1])
                    
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
        
        # Return the maximum width
        return maxWidth

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right.right.left = TreeNode(7)

print("Maximum width is ->", Solution().widthOfBinaryTree(root))