from collections import deque
from math import inf
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root):
        
        # Queue
        queue = deque()
        
        # Put the root in the queue
        queue.append(root)
        
        # To keep track of the level
        level = -1
        
        # While the queue is not empty
        while queue:
            
            # Update the level
            level += 1
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # To keep track of the value in the previous node
            prevNodeVal = -inf if level % 2 == 0 else inf
            
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If the level is even
                if level % 2 == 0:
                    
                    # This level needs to have all odd values
                    # Otherwise, return False
                    if node.val % 2 == 0: return False
                    
                    # This level needs to have values in strictly-increasing order
                    if node.val <= prevNodeVal: return False
                
                # If the level is odd
                else:
                    
                    # This level needs to have all even values
                    # Otherwise, return False
                    if node.val % 2 != 0: return False
                    
                    # This level needs to have values in strictly-decreasing order
                    if node.val >= prevNodeVal: return False
                    
                # Put the left and right children in the queue, if they exist
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
                # Update the value of the previous node
                prevNodeVal = node.val
                    
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
                
        # The Binary Tree is Even-Odd
        return True
                    
root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)
root.right.left.left = TreeNode(6)
root.right.right.right = TreeNode(2)

print("Output -> ", Solution().isEvenOddTree(root))
        