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
        
        # If not balanced, return -1
        if lHeight == -1 or rHeight == -1 or abs(lHeight - rHeight) > 1: return -1
        
        # Otherwise, return the height
        return max(lHeight, rHeight) + 1
    
    def isBalanced(self, root) -> bool:
        
        # if height is -1, it means that the tree is not balanced
        # Because a height of -1 will only be returned by the getHeight() function if the tree is not balanced
        return False if self.getHeight(root) == -1 else True

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