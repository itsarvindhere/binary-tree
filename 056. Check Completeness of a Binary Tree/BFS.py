from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root):
        
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # To keep track of the current level
        level = 0
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Save the original count
            count = nodesInCurrentLevel
            
            # Traverse all the nodes in the level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # A node cannot have a right child if there is no left child
                if not node.left and node.right: return False
                
                # If a node does not have a right child, there must not be any node after it in current level that has a child
                if not node.right and (queue and queue[0].left): return False
                
                # If the node has a left child, push to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push to the queue
                if node.right: queue.append(node.right)
                    
                # Update the node count
                nodesInCurrentLevel -= 1
            
            # If the queue is not empty, it means there are still one or more levels after current level
            # So, the current level should have all the nodes
            if queue and count < 2**level: return False
            
            # Update the level
            level += 1
                
        # The tree is a complete tree
        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print("Output -> ", Solution().isCompleteTree(root))