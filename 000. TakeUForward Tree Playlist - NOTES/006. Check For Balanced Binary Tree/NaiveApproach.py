class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    
    # HEIGHT OF A BINARY TREE
    def getHeight(self,root):
        
        # Base Case
        if not root: return 0
        
        # Height of left subtree
        lHeight = self.getHeight(root.left)
        
        # Height of right subtree
        rHeight = self.getHeight(root.right)
        
        # Get the maximum of the two (plus 1)
        return max(lHeight, rHeight) + 1
        
    
    
    def isBalanced(self, root) -> bool:
        
        # Base case
        if not root: return True
        
        # Get the height of left subtree
        lHeight = self.getHeight(root.left)
        
        # Get the height of right subtree
        rHeight = self.getHeight(root.right)
        
        # If the difference is > 1, it is not balanced
        if abs(lHeight - rHeight) > 1: return False
        
        # Otherwise, keep checking for next left and right subtrees
        isLeftSubtreeBalanced = self.isBalanced(root.left)
        isRightSubtreeBalanced = self.isBalanced(root.right)
        
        if not isLeftSubtreeBalanced or not isRightSubtreeBalanced: return False
        
        return True

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print("Is this a Height Balanced Binary Tree ->", Solution().isBalanced(root))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)


print("Is this a Height Balanced Binary Tree ->", Solution().isBalanced(root))