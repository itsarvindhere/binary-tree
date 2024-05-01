from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root):
        
        
        # Queue
        queue = deque()
        queue.append(root)
        
        # To keep track of the levels
        level = -1
        
        # While the queue is not empty
        while queue:
            
            # Update the level
            level += 1
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # If this is an odd level
            # Reverse the node values
            if level % 2 != 0:
                i,j = 0, nodesInCurrentLevel - 1
                while i < j:
                    queue[i].val, queue[j].val = queue[j].val, queue[i].val
                    i += 1
                    j -= 1
                    
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
        # Return the root of the tree
        return root

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)

print("Output -> ", Solution().reverseOddLevels(root))