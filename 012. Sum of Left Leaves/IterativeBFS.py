from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def sumOfLeftLeaves(self, root):
        
        # Total Sum to return
        totalSum = 0
        
        # Queue, initialized with the root node and a flag to indicate if it is the left child
        queue = deque()
        queue.append((root, False))
        
        # While the queue is not empty
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
            
                # Pop the node in front of the queue, along with its flag
                node, isLeftNode = queue.popleft()

                # If this is a leaf node and also a left leaf node
                if not node.left and not node.right and isLeftNode: totalSum += node.val

                # Push the right child in the queue
                if node.right: queue.append((node.right, False))

                # Push the left child in the queue
                if node.left: queue.append((node.left, True))
                    
                # Update the node count
                nodesInCurrentLevel -= 1
        
        # Return the total Sum
        return totalSum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Total Sum of Left Leaves -> ", Solution().sumOfLeftLeaves(root))