from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        # Total Sum to return
        totalSum = 0
        
        # Queue
        queue = deque()
        queue.append([root, None])
        
        # While the queue is not empty
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue along with its parent (which is the grandparent of its children)
                node, parent  = queue.popleft()
                
                # Push the left child in the queue
                if node.left: 
                    queue.append([node.left, node])
                    
                    # If the node's parent is an even valued node
                    # Add to the total sum
                    if parent and parent.val % 2 == 0: totalSum += node.left.val
                    
                # Push the right child in the queue
                if node.right: 
                    queue.append([node.right, node])
                    # If the node's parent is an even valued node
                    # Add to the total sum
                    if parent and parent.val % 2 == 0: totalSum += node.right.val
                
                # Update the count
                nodesInCurrentLevel -= 1
        
        # Finally, return the total sum
        return totalSum

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

print("Output -> ", Solution().sumEvenGrandparent(root))