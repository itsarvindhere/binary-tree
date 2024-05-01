
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    
    # Helper function for DFS traversal
    def dfs(self, root, values):
        
        # Base Case
        if not root: return
        
        # Update the values set
        values.add(root.val)
        
        # Update the left and right child values
        if root.left: root.left.val = (2 * root.val) + 1
        if root.right: root.right.val = (2 * root.val) + 2
        
        # Traverse left
        self.dfs(root.left, values)
        
        # Traverse right
        self.dfs(root.right, values)

    def __init__(self, root):
        
        # A set of values
        self.values = set()
        
        # Traverse the tree in DFS order
        # Update the root node's value to 0
        root.val = 0
        self.dfs(root, self.values)
        

    def find(self, target: int) -> bool:
        
        # Return true if the "target" exists in the set
        return target in self.values


root = TreeNode(-1)
root.right = TreeNode(-1)
findElements = FindElements(root); 

print(findElements.find(1))
print(findElements.find(2))