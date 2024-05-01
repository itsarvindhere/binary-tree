# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        # Base Case
        if not root: return 0

        # If current node is a leaf node
        # And we have the sum from root to this current node equal to targetSum
        # Then it means we found one valid path so we can return True
        if not root.left and not root.right and root.val == targetSum: return True

        # Make a recursive call for the left subtree to see if there exists a path
        # The target that we will pass will be "targetSum - root.val"
        # It means, we already found "root.val" so the remaining is what we have to find on left subtree
        isPathOnLeft = self.hasPathSum(root.left, targetSum - root.val)

        # If there exists a path on the left, we can straight away return True
        if isPathOnLeft: return True

        # Make a recursive call for the right subtree to see if there exists a path
        isPathOnRight = self.hasPathSum(root.right, targetSum - root.val)

        # Return True or False, based on whether a valid path exists on right or not
        return isPathOnRight

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print("Output ->", Solution().hasPathSum(root, 22))