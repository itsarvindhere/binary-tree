from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    
    def goodNodes(self, root: TreeNode) -> int:
        
        # Count of good nodes
        count = 0
        
        # Queue, initially with the root node and the maximum on current path so far
        queue = deque()
        queue.append([root, root.val])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node, maxSoFar = queue.popleft()

                # If the node has a value >= maxSoFar, then it is a good node
                if node.val >= maxSoFar: 
                    count += 1
                    maxSoFar = node.val

                # If the node has a left child, push it to the queue
                if node.left: queue.append([node.left, maxSoFar])

                # If the node has a right child, push it to the queue
                if node.right: queue.append([node.right, maxSoFar])
                
                # Update the count
                nodesInCurrentLevel -= 1
            
        # Return the count
        return count

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print("Output -> ", Solution().goodNodes(root))