class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Pre-Order Traversal
    def preOrder(self, root, p, q, lca):
        
        # If node is Null or node is p or node is q
        # We will return the node itself
        if not root or root == p or root == q: return root
        
        # Otherwise, check on left if we have p or q
        nodeMatchedOnLeft = self.preOrder(root.left, p, q, lca)
        
        # Check on Right if we have p or q
        nodeMatchedOnRight = self.preOrder(root.right, p, q, lca)
        
        # If there is "p" or "q" on left and also on right
        # It means the current "root" is the lowest common ancestor of these nodes
        if nodeMatchedOnLeft and nodeMatchedOnRight: lca[0] = root
            
        # Otherwise, if there is "p" or "q" on one side but not on the other
        # Then it means the lowest common ancestor will be the node found on that side
        else: lca[0] = nodeMatchedOnLeft or nodeMatchedOnRight
        
        # Return the lowest common Ancestor 
        # This return value is going to be used as the result of current call, 
        # in previous calls of this recursive function
        return lca[0]
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # To keep track of the lowest common ancestor
        lca = [root]
        
        # Call the recursive DFS function
        self.preOrder(root, p, q, lca)
                
        # Finally, return the lowest common ancestor
        return lca[0]

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = root.left.right.left = TreeNode(7)
q = root.left.right.right = TreeNode(4)

print("Lowest Common Ancestor ->", Solution().lowestCommonAncestor(root, p, q ).val)