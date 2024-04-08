class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        
        # Base Case
        if not root: return
        
        # Invert the left subtree
        invertedLeft = self.invertTree(root.left)
        
        # Invert the right subtree
        invertedRight = self.invertTree(root.right)
        
        # At this point, left and right subtrees are inverted
        # So, assign the left inverted subtree as the right child
        # And assign the right inverted subtree as the left child
        root.left = invertedRight
        root.right = invertedLeft
        
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