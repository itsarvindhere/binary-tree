from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def maxDepth(self, root) -> int:
        
        # Maximum depth to return
        depth = 0
        
        # If there is no node at all, depth is 0
        if not root: return depth
        
        # Queue
        queue = deque()
        
        # Initially, queue has the root node and we are at the first level
        queue.append(root)
        
        # While the queue is not empty
        while queue:

            # Increment the depth/level
            depth += 1
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # Traverse all the nodes in current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If the node has a left child, push it in the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it in the queue
                if node.right: queue.append(node.right)
                    
                # Update the count of nodes for current level
                nodesInCurrentLevel -= 1
            
        # Finally, return the maximum depth
        return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Maximum depth of the tree is -> ", Solution().maxDepth(root))

