# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # To get the data about parent nodes
    def getParentNodes(self, root, parent, node1, x, parentNodes):
        
        # Base Case
        if not root: return
        
        # Update the parent node
        if parent: parentNodes[root] = parent
            
        if root.val == x: node1[0] = root
            
        # Traverse left
        self.getParentNodes(root.left, root, node1, x, parentNodes)
        
        # Traverse right
        self.getParentNodes(root.right, root, node1, x, parentNodes)
        
    # Helper function to count nodes in a tree rooted at "root"
    def count(self, root, node1, parentNodes, visited):
        
        # Base Case
        if not root or root == node1 or root in visited: return 0
        
        # Add to the visited set
        visited.add(root)
        
        # Traverse top
        topCount = 0
        if root in parentNodes: 
            topCount = self.count(parentNodes[root], node1, parentNodes, visited)
        
        # Traverse left
        leftCount = self.count(root.left, node1, parentNodes, visited)
        
        # Traverse right
        rightCount = self.count(root.right, node1, parentNodes, visited)
        
        # Return the total count
        return topCount + leftCount + 1 + rightCount
    
    def btreeGameWinningMove(self, root, n: int, x: int):
        
        # To keep track of the parent nodes
        parentNodes = {}
        
        # Also get the node that first player selected
        node1 = [None]
        
        # Traverse the tree and get information about parent nodes
        self.getParentNodes(root, None, node1, x, parentNodes)
        
        # Count of nodes in the subtree with root = parent of node1 (if it is not root itself)
        countTop = 0
        if node1[0] in parentNodes: countTop = self.count(parentNodes[node1[0]], node1[0], parentNodes, set())
        
        # Count of nodes in the subtree with root = left child of node1 (if it exists)
        countLeft = self.count(node1[0].left, node1[0], parentNodes, set())
        
        # Count of nodes in the subtree with root = right child of node1( (if it exists)
        countRight = self.count(node1[0].right, node1[0], parentNodes, set())
        
        # The second player can only win if among all the three subtrees around the node that "x" has chosen,
        # One subtree has more nodes than the other two
        return countTop > countLeft + countRight or countLeft > countTop + countRight or countRight > countTop + countLeft

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

n = 11
x = 3

print("Can second player win? -> ", Solution().btreeGameWinningMove(root, n, x))