class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def flatten(self, root):
        
        # Base Case
        if not root: return
        
        # Flatten the left subtree
        leftSubtree = self.flatten(root.left)
        
        # Flatten the right subtree
        rightSubtree = self.flatten(root.right)
        
        # Make the left child as Null
        root.left = None
        
        # Make the right child as the flattened right subtree
        root.right = rightSubtree
        
        # If we have a flattened left subtree
        if leftSubtree:
            
            # Make it the right child of root
            root.right = leftSubtree
            
            # Traverse till the end of this flattened tree
            while leftSubtree.right: leftSubtree = leftSubtree.right
                
            # And make its right child as the flattened right subtree
            leftSubtree.right = rightSubtree
        
        # Finally, return the root node
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

Solution().flatten(root)