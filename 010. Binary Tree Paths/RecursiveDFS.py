# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Pre Order Traversal
    def preOrder(self, root, paths, currentPath):
        
        # Base case
        if not root: return 
        
        # Push the root node's value to the current path
        currentPath.append(str(root.val))
        
        # Is the current "root" node a leaf node?
        if not root.left and not root.right: return True
        
        # Traverse left to see if there is a leaf node on left side
        isLeafNodeOnLeft = self.preOrder(root.left, paths, currentPath)
        
        # If there is a leaf node on the left side
        if isLeafNodeOnLeft: 
            
            # Take the current path and push to the paths list
            paths.append("->".join(currentPath))
            
            # Pop from the current path to remove the leaf node that we have already covered
            currentPath.pop()
        
        # Traverse right
        isLeafNodeOnRight = self.preOrder(root.right, paths, currentPath)
        
        # If there is a leaf node on the right side
        if isLeafNodeOnRight: 
            
            # Take the current path and push to the paths list
            paths.append("->".join(currentPath))
            
            # Pop from the current path to remove the leaf node that we have already covered
            currentPath.pop()
        
        # Finally, once we have covered both the left and right of the current node, 
        # we can pop this node from the current path
        currentPath.pop()
    
    
    def binaryTreePaths(self, root):
        
        # # If there is a single node in the Binary Tree
        if not root.left and not root.right: return [str(root.val)]
        
        # To keep all the paths in the tree
        paths = []
        
        # To keep track of the current path
        currentPath = []
        
        # Call the Pre Order Traversal Recursive Function
        self.preOrder(root, paths, currentPath)
        
        # Return all the paths
        return paths


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right= TreeNode(5)

print("Root to Leaf Paths are -> ", Solution().binaryTreePaths(root))