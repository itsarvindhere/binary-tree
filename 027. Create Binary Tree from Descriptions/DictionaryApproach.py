# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions):
        
        # A Dictionary to keep value and the respective node
        nodes = {}
        
        # All the node values that have parents
        nodesWithParents = set()
        
        # Iterate over the descriptions list
        for parent, child, isLeft in descriptions:
            
            # Push the "child" to the set
            nodesWithParents.add(child)
            
            # If parent does not exist in the dictionary yet, put it
            if parent not in nodes: nodes[parent] = TreeNode(parent)
                
            # If child does not exist in the dictionary yet, put it
            if child not in nodes: nodes[child] = TreeNode(child)
                
            # If "isLeft" is 1, then "child" is the left child of "parent"
            if isLeft == 1: nodes[parent].left = nodes[child]
            else: nodes[parent].right = nodes[child]
                
        # Get the root node's value
        # It is the node that has no parent
        # This means, the root node's value should not be present in the set
        root = -1
        for parent, child, isLeft in descriptions:
            if parent not in nodesWithParents: 
                root = parent
                break
        
        # Return the root node at the end
        return nodes[root]


descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

print("Output -> ", Solution().createBinaryTree(descriptions))