class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Pre-Order Traversal to get the path from root node to a specific node
    def preOrder(self, root, target, path):
        
        # Base case
        if not root: return False
        
        # Put the root node in path
        path.append(root)
        
        # If this is the target node, return True
        if root == target: return True
        
        # If not, then make recursive calls to check if the target node is on left or right side
        isNodeOnLeft = self.preOrder(root.left, target, path)
        
        # If the target node is on left side, return True
        if isNodeOnLeft: return True
        
        isNodeOnRight = self.preOrder(root.right, target, path)
        
        # If the target node is on right side, return True
        if isNodeOnRight: return True
        
        # If target node is not on left or right, 
        # it means current node "root" cannot be in the path to target node
        path.pop()
        return False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        rootToP, rootToQ = [], []
        
        self.preOrder(root, p, rootToP)
        self.preOrder(root, q, rootToQ)
        
        # Two Pointers for each of the two lists
        left,right = 0, 0
        
        # Lowest Common Ancestor
        lca = root
        
        while left < len(rootToP) and right < len(rootToQ):
            # If the nodes are the same at left and right, update the lca
            # And update the pointers since we want "lowest" common ancestor, Not the highest
            if rootToP[left] == rootToQ[right]: 
                lca = rootToP[left]
                left += 1
                right += 1
            # Otherwise, we can exit
            else: break
                
        # Finally, return the lowest common ancestor
        return lca

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