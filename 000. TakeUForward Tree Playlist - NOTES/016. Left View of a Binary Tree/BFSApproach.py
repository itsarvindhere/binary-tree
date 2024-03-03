from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftSideView(self, root):
        
        # QUEUE
        queue = deque()
        
        # Output list to return
        output = []
        
        # If there is no node
        if not root: return output
        
        # Put the root node in the queue
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Leftmost node's value in current level
            leftmostNodeValue = None
            
            while nodesInCurrentLevel > 0:
                
                # Pop the front node
                node = queue.popleft()
                
                # Update the leftmost node value for current level
                if leftmostNodeValue is None: leftmostNodeValue = node.val
                
                # Push left and right child in the queue if they exist
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
                
            # Push the leftmost node value in the output list
            output.append(leftmostNodeValue)
        
        # Finally, return the output list
        return output

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

print("Output -> ", Solution().leftSideView(root))