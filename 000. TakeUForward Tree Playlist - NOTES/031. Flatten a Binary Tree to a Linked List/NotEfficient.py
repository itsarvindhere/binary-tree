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
        self.flatten(root.left)
        
        # Flatten the right subtree
        self.flatten(root.right)
        
        # If we have a flattened left subtree
        if root.left:
            
            # Save the right subtree
            prevRight = root.right
            
            # Make it the right child of root
            root.right = root.left
            
            # Traverse till the end of this flattened tree
            temp = root.left
            while temp.right: temp = temp.right
                
            # And make its right child as the flattened right subtree
            temp.right = prevRight
            
        # Finally, do not forget to set the left child as Null
        root.left = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

Solution().flatten(root)