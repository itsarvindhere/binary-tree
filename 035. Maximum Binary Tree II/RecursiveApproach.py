# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    def insertIntoMaxTree(self, root, val):
        
        # Base Case
        if not root: return TreeNode(val)
        
        # If the root of current tree has a value smaller than "val"
        # Then, this subtree will become the left child of this new node
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        
        # If the root node's value is greater than "val"
        # It means, the new node will be inserted in the right subtree
        root.right = self.insertIntoMaxTree(root.right, val)
        
        # Finally, we can return the root node
        return root
        

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)

val = 3

print("Output -> ", Solution().insertIntoMaxTree(root, val))
        
        
        