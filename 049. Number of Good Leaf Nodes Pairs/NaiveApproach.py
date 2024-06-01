# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper method to get the parent nodes
    def getParentNodes(self, root, parent, parentNodes):
        
        # Base Case
        if not root: return
        
        # Update the dictionary
        if parent: parentNodes[root] = parent
            
        # Traverse left
        self.getParentNodes(root.left, root, parentNodes)
        
        # Traverse right
        self.getParentNodes(root.right, root, parentNodes)
        
    # Helper method to traverse the tree and count good leaf node pairs
    def count(self, root, count, parentNodes, visited, currDistance, distance):
        
        # If the node is None
        # OR
        # If the node has already been visited
        # OR
        # The current distance is already > distance
        if not root or root in visited or currDistance > distance: return
        
        # Add to the visited set
        visited.add(root)
        
        # If this is a root node, we found one pair
        if not root.left and not root.right: count[0] += 1
        
        # Traverse left, right and top
        if root in parentNodes and parentNodes[root] not in visited: 
            self.count(parentNodes[root], count, parentNodes, visited, currDistance + 1, distance)
            
        if root.left not in visited: 
            self.count(root.left, count, parentNodes, visited, currDistance + 1, distance)
            
        if root.right not in visited:
            self.count(root.right, count, parentNodes, visited, currDistance + 1, distance)
        
        
    # Helper method to traverse the tree
    # And count the good leaf nodes pairs
    def dfs(self, root, count, parentNodes, distance):
        
        # Base Case
        if not root: return
        
        # If this is a leaf node
        if not root.left and not root.right and root in parentNodes: 
            
            # Traverse the tree, starting from the parent of this leaf node
            # And keep track of the distance
            visited = set()
            visited.add(root)
            self.count(parentNodes[root], count, parentNodes, visited, 1, distance)
    
        # Traverse left
        self.dfs(root.left, count, parentNodes, distance)
        
        # Traverse right
        self.dfs(root.right, count, parentNodes, distance)
    
    def countPairs(self, root, distance: int) -> int:
        
        # To keep track of the parent nodes of each node
        parentNodes = {}
        
        # DFS Traversal to get the data about the parent node of each node
        self.getParentNodes(root, None, parentNodes)
        
        # To get the count of good leaf node pairs
        count = [0]
        
        # Traverse the tree to get the count
        self.dfs(root, count, parentNodes, distance)
        
        # Return the count of good leaf node pairs
        return count[0] // 2

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

distance = 3

print("Output -> ", Solution().countPairs(root, distance))