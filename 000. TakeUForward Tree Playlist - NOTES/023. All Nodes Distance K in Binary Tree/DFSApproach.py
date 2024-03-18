# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Pre Order Traversal to find root nodes for every node
    def getRootNodes(self, root, parentNodes):
        
        # BASE CASE
        if not root: return
        
        # Update the dictionary
        if root.left: parentNodes[root.left] = root
        if root.right: parentNodes[root.right] = root
            
        # Traverse left
        self.getRootNodes(root.left, parentNodes)
        
        # Traverse right
        self.getRootNodes(root.right, parentNodes)
        
    # Pre Order Traversal to get all the nodes at a distance of "k" from "root" node
    def getDistance(self, root, k, visited, parentNodes, output):
        
        # BASE CASE
        # If we are at Null node or,
        # If we have already traversed the current node, return
        if not root or root in visited: return
        
        # Add the node to visited set
        visited.add(root)
        
        # If the distance is reached, put the node value in output list and return
        if k == 0: 
            output.append(root.val)
            return
        
        # Traverse towards parent node (if the parent node exists)
        if root in parentNodes: self.getDistance(parentNodes[root], k - 1, visited, parentNodes, output)
            
        # Traverse left
        self.getDistance(root.left, k - 1, visited, parentNodes, output)
        
        # Traverse right
        self.getDistance(root.right, k - 1, visited, parentNodes, output)
        
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        
        # A Dictionary to keep the parent nodes of every node in the Tree
        # This will be useful when from any node, we have to traverse towards top
        # Because in a Binary Tree, we can easily traverse top to bottom from any node
        # But not from bottom to top because a node does not contain any data about who the parent is
        # Only from the parent we can know who the children are
        parentNodes = {}
        self.getRootNodes(root, parentNodes)
                
        # At this point, we know for each node, what is the parent
        # Now, from the "target" node, we will traverse outwards. That is, left, right and parent
        
        # Set to keep track of visited nodes
        visited = set()
        
        # Output list
        output = []
        self.getDistance(target, k, visited, parentNodes, output)
            
        # Return the output list
        return output
        

root = TreeNode(3)
target = root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

k = 2

print("Nodes at K distance -> ", Solution().distanceK(root, target,k))