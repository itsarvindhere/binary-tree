from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        
        # The output list to return
        output = []
        
        # If there are no nodes
        if not root: return output
        
        # A Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are the current level
            nodesInCurrentLevel = len(queue)
            
            # List of node values in current level
            currLevelNodes = []
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Push to the current level's list
                currLevelNodes.append(node.val)
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Finally, push to the output list
            output.append(currLevelNodes)
            
        # Return the output list, in reversed order
        return reversed(output)
        
                
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Output -> ", Solution().levelOrderBottom(root))