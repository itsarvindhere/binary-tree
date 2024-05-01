
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    
    # Helper function for DFS traversal
    def dfs(self, root, values):
        
        # Stack, initially with the root node
        stack = [root]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack
            node = stack.pop()
            
            # Update the values set
            values.add(node.val)
            
            # If there is a right child, push to the stack
            if node.right:
                stack.append(node.right)
                node.right.val = (2 * node.val) + 2
                
            # If there is a left child, push to the stack
            if node.left:
                stack.append(node.left)
                node.left.val = (2 * node.val) + 1

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