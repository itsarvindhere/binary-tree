from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def maxAncestorDiff(self, root) -> int:
        
        # Maximum difference to return
        maxDiff = 0
        
        # Queue, initially with the root node
        queue = deque()
        
        # The other two values indicate the minimum and maximum ancestor values so far (Initially, root values)
        queue.append([root, root.val, root.val])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node, minAncestorValue, maxAncestorValue = queue.popleft()
                
                # Update the maximum difference accordingly
                maxDiff = max(maxDiff, abs(node.val - minAncestorValue), abs(node.val - maxAncestorValue))
                
                # If there is a left child, push it to the queue
                if node.left: queue.append([node.left, min(minAncestorValue, node.val), max(maxAncestorValue, node.val)])
                    
                #  If there is a right child, push it to the stack
                if node.right: queue.append([node.right, min(minAncestorValue, node.val), max(maxAncestorValue, node.val)])
                
                # Update the count
                nodesInCurrentLevel -= 1
        
        # Return the maximum difference
        return maxDiff

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
root.left.right.left = TreeNode(4)
root.right.right.right = TreeNode(7)

print("Output -> ", Solution().maxAncestorDiff(root))