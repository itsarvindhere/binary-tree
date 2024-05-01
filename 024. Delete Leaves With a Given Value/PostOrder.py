
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def removeLeafNodes(self, root, target: int):
        
        # Base Case
        if not root: return None
        
        # Delete the required nodes in left subtree and return the remaining tree
        root.left = self.removeLeafNodes(root.left, target)
        
        # Delete the required nodes in the right subtree and return the remaining tree
        root.right = self.removeLeafNodes(root.right, target)
        
        # If after deletion of nodes on left or right, current "root" node becomes a leaf node with value = target
        # So, we have to remove it as well in that case
        if not root.left and not root.right and root.val == target: return None
        
        # Finally, return the root node
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

target = 2

print("Output ->", Solution().removeLeafNodes(root, target))