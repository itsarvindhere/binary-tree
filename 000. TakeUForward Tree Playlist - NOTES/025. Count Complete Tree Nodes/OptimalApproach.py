
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to get the level at which the leftmost node is present
    def getLeftmostNodeLevel(self,root):
        
        # Level
        level = 0
        
        # Get the level
        while root:
            level += 1
            root = root.left
        
        # Return the level
        return level
    
    # Helper function to get the level at which the rightmost node is present
    def getRightmostNodeLevel(self,root):
        
        # Level
        level = 0
        
        # Get the level
        while root:
            level += 1
            root = root.right
        
        # Return the level
        return level
        
    def countNodes(self, root) -> int:
        
        # BASE CASE
        if not root: return 0
        
        # Get the levels of leftmost and rightmost nodes for tree with root node as "root"
        leftLevel = self.getLeftmostNodeLevel(root)
        rightLevel = self.getRightmostNodeLevel(root)
        
        # If the levels are same, it means we can directly find the number of nodes as "2^h - 1"
        # Because if levels are same, it means the tree with root as "root" is a Perfect Binary Tree
        if leftLevel == rightLevel: return 2**leftLevel - 1
        
        # If the levels aer not the same, recursively call the countNodes method for left and right subtree
        # And then, whatever left and right calls return, we just need to add 1 to that (because we need to accomodate "root" node)
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

print("Number of nodes ->", Solution().countNodes(root))