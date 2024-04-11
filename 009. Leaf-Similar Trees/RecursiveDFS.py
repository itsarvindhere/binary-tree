class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # DFS to get all the leaf values
    def dfs(self, root, leafNodes):
        
        # Base case
        if not root: return
        
        # If this is a leaf node, put it in the list
        if not root.left and not root.right: leafNodes.append(root.val)
            
        # Traverse left
        self.dfs(root.left, leafNodes)
        
        # Traverse right
        self.dfs(root.right, leafNodes)
    
    
    def leafSimilar(self, root1, root2):
        
        # Leaf node sequent for root1
        root1Sequence = []
        
        # Leaf node sequent for root2
        root2Sequence = []
        
        self.dfs(root1, root1Sequence)
        self.dfs(root2, root2Sequence)
        
        # Compare the two
        return root1Sequence == root2Sequence


root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)


root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

print("Output -> ", Solution().leafSimilar(root1, root2))