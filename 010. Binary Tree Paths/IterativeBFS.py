from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def binaryTreePaths(self, root):
        
        # If there is a single node in the Binary Tree
        if not root.left and not root.right: return [str(root.val)]
        
        # To keep all the paths in the tree
        paths = []
        
        # A Queue
        queue = deque()
        
        # Initialize the queue with the root node
        # We will push a pair to the queue
        # The first value is the node itself
        # And the second value is the path so far from the root to that node
        queue.append([root, [str(root.val)]])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node, currentPath = queue.popleft()
                
                # If this is the leaf node
                if not node.left and not node.right:
                    # Take the path till itself and push it to the output list
                    paths.append("->".join(currentPath))
                
                # If the node has a left child push it to the queue
                if node.left: 
                    newPath = currentPath[:]
                    newPath.append(str(node.left.val))
                    queue.append([node.left, newPath])
                    
                # If the node has a right child push it to the queue
                if node.right: 
                    newPath = currentPath[:]
                    newPath.append(str(node.right.val))
                    queue.append([node.right, newPath])
                    
                # Decrement the nodes in current level
                nodesInCurrentLevel -= 1
                
        # Return all the paths
        return paths


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right= TreeNode(5)

print("Root to Leaf Paths are -> ", Solution().binaryTreePaths(root))