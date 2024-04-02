
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def flatten(self, root):
        
        # Base Case
        if not root: return

        # Recursive call for flattening the left subtree and also to get the last node in this tree
        lastNodeOnLeft = self.flatten(root.left)

        # Recursive call for flattening the right subtree and also to get the last node in this tree
        lastNodeOnRight = self.flatten(root.right)
        
        # If the left subtree exists, we will have the last node in this subtree at this point
        # Moreover, the left and right subtrees will be flattened already at this point
        # So, make the flattened left subtree point to the right of "root"
        # And attach the previous right of the root to the "lastNodeOnLeft"
        if lastNodeOnLeft: 
            prevRight = root.right
            root.right = root.left
            lastNodeOnLeft.right = prevRight
        
        # Finally, do not forget to make the left child as Null
        root.left = None
        
        # Return the last node in right subtree if it exist
        if lastNodeOnRight: return lastNodeOnRight
        
        # If it does not, return the last node in left subtree
        elif lastNodeOnLeft: return lastNodeOnLeft
        
        # Otherwise, it means the current "root" is the leaf node so return itself
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

Solution().flatten(root)