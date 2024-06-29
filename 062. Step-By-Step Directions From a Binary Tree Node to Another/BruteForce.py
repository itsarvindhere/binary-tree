# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to get the parentNodes for each node
    # And also to get the startNode and endNode (since we are only given values)
    def getParentNodes(self, root, startValue, destValue, startNode, destNode, parent, parentNodes):
        
        if not root: return None
        
        # Update the parent of the current node
        if parent: parentNodes[root] = parent
        
        # If current valye is equal to startValue or destValue
        if root.val == startValue or root.val == destValue: 
            if root.val == startValue: startNode[0] = root
            else: destNode[0] = root
        
        # Traverse left
        self.getParentNodes(root.left, startValue, destValue, startNode, destNode, root, parentNodes)
        
        # Traverse right
        self.getParentNodes(root.right, startValue, destValue, startNode, destNode, root, parentNodes)
    
    # Helper function to get the path
    def getPath(self, startNode, destNode, parentNodes, currPath, finalPath, visited):
        
        # Base Case
        if not startNode or finalPath[0] or startNode in visited: return
        
        # Add to the visited set
        visited.add(startNode)
        
        # If current startNode is the destNode, it means we reached the destNode so we got the path
        if startNode == destNode:
            finalPath[0] = "".join(currPath)
            return
        
        leftPath, rightPath, topPath = currPath[:], currPath[:], currPath[:]
        leftPath.append('L')
        rightPath.append('R')
        topPath.append('U')
        
        # Traverse left
        self.getPath(startNode.left, destNode, parentNodes, leftPath, finalPath, visited)
        
        # Traverse right
        self.getPath(startNode.right, destNode, parentNodes, rightPath, finalPath, visited)
        
        # Traverse top
        if startNode in parentNodes: self.getPath(parentNodes[startNode], destNode, parentNodes, topPath, finalPath, visited)
    
    
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        
        # Start and dest Nodes
        startNode, destNode = [None], [None]
        
        # To keep track of the parent nodes
        parentNodes = {}
        
        # Get the details of parentNodes and also the start and dest Nodes
        self.getParentNodes(root, startValue, destValue, startNode, destNode, None, parentNodes)
        
        # Path to return
        path = [""]

        # Get the path from "startNode" to "destNode"
        self.getPath(startNode[0], destNode[0], parentNodes, [], path, set())
             
        # Return the path
        return path[0]

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

startValue, destValue = 3,6

print("Output -> ", Solution().getDirections(root, startValue, destValue))