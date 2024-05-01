# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # DFS
    def dfs(self, root, parent, grandParent, totalSum):
        
        # Base Case
        if not root: return 
        
        # If the grandParent exists and its value is even
        if grandParent and grandParent.val % 2 == 0: totalSum[0] += root.val
        
        # Traverse left
        self.dfs(root.left, root, parent, totalSum)
        
        # Traverse right
        self.dfs(root.right, root, parent, totalSum)
    
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        # Total Sum to return
        totalSum = [0]
        
        # Call the DFS Function
        self.dfs(root, None, None, totalSum)
        
        # Return the total sum
        return totalSum[0]

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

print("Output -> ", Solution().sumEvenGrandparent(root))