from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ******************************
# BFS SOLUTION - RIGHT TO LEFT
# ******************************
class Solution:
    def findBottomLeftValue(self, root):
        
        # Queue
        queue = deque()
        
        # Put the root node in the queue initially
        queue.append(root)
        
        # Initialize the bottom left value as root
        bottomLeftVal = root.val
        
        # While the queue is not empty
        while queue:
            
            # Update the bottom left value
            bottomLeftVal = queue[0].val
            
            # Pop the node in front and push its left and right children in queue if they exist
            # We will push "right" first and then "left"
            node = queue.popleft()
            
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)
                
        # Finally, return the bottom left node's value
        return bottomLeftVal

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)

print("Leftmost node in last level ->", Solution().findBottomLeftValue(root))