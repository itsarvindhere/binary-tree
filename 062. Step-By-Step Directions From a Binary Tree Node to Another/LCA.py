# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to find the LCA
    def lca(self, root, p, q):
        
        # Base Case
        if not root: return None
        
        if root.val == p or root.val == q: return root
        
        # Check if node "p" or "q" exist on left side of the node "root"
        nodeOnLeft = self.lca(root.left, p, q)
        
        # Check if node "p" or "q" exist on right side of the node "root"
        nodeOnRight = self.lca(root.right, p, q)
        
        # If there exists "p" or "q" on left and right
        # Then it means "root" is the lca of "p" and "q"
        if nodeOnLeft and nodeOnRight: return root
        
        # If there is "p" or "q" on one side but not on the other
        # It means, the side on which we have "p" or "q" will give us the LCA
        return nodeOnLeft if nodeOnLeft else nodeOnRight
    
    # Helper function to get the paths from start to lca and from lca to dest
    def getPaths(self, root, startValue, destValue, currPath, startToLca, lcaToDest):
        
        # Base Case
        if not root or (startToLca[0] and lcaToDest[0]): return
        
        # If current value is the start or dest value
        if root.val == startValue or root.val == destValue: 
            if root.val == startValue: startToLca[0] = currPath[:]
            else: lcaToDest[0] = currPath[:]
        
        # Traverse left
        currPath.append('L')
        self.getPaths(root.left, startValue, destValue, currPath, startToLca, lcaToDest)
        
        currPath.pop()
        
        # Traverse right
        currPath.append('R')
        self.getPaths(root.right, startValue, destValue, currPath, startToLca, lcaToDest)
    
        currPath.pop()
    
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        
        # Get the LCA of "startValue" and "destValue"
        lca = self.lca(root, startValue, destValue)
        
        # Now, we need two paths -> "startValue to lca" and "lca to destValue"
        startToLca = [[]]
        lcaToDest = [[]]
        self.getPaths(lca, startValue, destValue, [], startToLca, lcaToDest)
        
        # The final path to build
        finalPath = []
        for direction in startToLca[0]: finalPath.append("U")
        for direction in lcaToDest[0]: finalPath.append(direction)
        
        return "".join(finalPath)

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

startValue, destValue = 3,6

print("Output -> ", Solution().getDirections(root, startValue, destValue))