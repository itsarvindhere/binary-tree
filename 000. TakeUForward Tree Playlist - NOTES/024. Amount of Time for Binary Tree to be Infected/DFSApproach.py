from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive DFS function to get the parent nodes of every node
    # And to also get the startNode (with value = start)
    def getParentNodes(self, root, parentNodes, startNode, start):
        
        # BASE CASE
        if not root: return
        
        # Update the dictionary for parent nodes
        if root.left: parentNodes[root.left] = root
        if root.right: parentNodes[root.right] = root
            
        # If this is the target node, update the startNode
        if root.val == start: startNode[0] = root
            
        # Traverse left
        self.getParentNodes(root.left, parentNodes, startNode, start)
        
        # Traverse right
        self.getParentNodes(root.right, parentNodes, startNode, start)
        
        
    # Recursive DFS function to get the minutes needed for all the nodes to get infected
    def getMinutes(self, node, visited, parentNodes, currentTime, minutes):
        
        # BASE CASE
        if not node or node in visited: return
        
        # Add to the visited set
        visited.add(node)
        
        # Update the minutes
        minutes[0] = max(minutes[0], currentTime)
        
        # Traverse towards top
        if node in parentNodes: self.getMinutes(parentNodes[node], visited, parentNodes, currentTime + 1, minutes)
            
        # Traverse left
        self.getMinutes(node.left, visited, parentNodes, currentTime + 1, minutes)
        
        # Traverse right
        self.getMinutes(node.right, visited, parentNodes, currentTime + 1, minutes)
    
    def amountOfTime(self, root, start: int) -> int:
        
        # First, for each node, we will keep track of what is the parent node
        # Since we have to traverse in all the directions from the infected node
        # That is, towards top, left and right
        parentNodes = {}
        
        # The startNode with value == start
        startNode = [None]
        self.getParentNodes(root, parentNodes, startNode, start)
        
        # To keep track of the minutes
        minutes = [-1]
        
        # To keep track of visited nodes. In other words, the nodes that are already infected
        visited = set()
        self.getMinutes(startNode[0], visited, parentNodes, 0, minutes)

        # Return the minutes
        return minutes[0]


root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(2)

print("Output -> ", Solution().amountOfTime(root,3))