from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        
        # If there are no nodes
        if not root: return

        # Stack, initially with root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many Nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()

                # Push the left child
                if node.left: queue.append(node.left)
                    
                # Push the right child
                if node.right: queue.append(node.right)
                
                # Swap the left and right subtrees
                node.left, node.right = node.right, node.left
                
                # Update the count
                nodesInCurrentLevel -= 1
        
        # Finally, return the root node
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Output -> ", Solution().invertTree(root))