# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str):
        # Length of the list
        n = len(traversal)
        
        # Stack
        stack = [] 
        
        # Root node
        root = None
        
        # Iterate over the list
        i = 0
        while i < n:
            
            # Get the depth
            depth = 0
            while i < n and traversal[i] == "-": 
                depth += 1
                i += 1
                
            # Get the value
            val = []
            while i < n and traversal[i] != "-":
                val.append(traversal[i])
                i += 1
                
            # Value to a string
            val = "".join(val)
                
            # Current node
            node = TreeNode(val)
            
            # If the depth is 0, it is the root node
            if depth == 0: root = node
                
            # Otherwise
            else: 
                
                # If the current depth is smaller than previous, we need to pop all the previous nodes that have a greater depth
                while stack and stack[-1][1] >= depth: stack.pop()
                    
                # If the node on top of stack does not have a left child, then current node is the left child
                if not stack[-1][2]: 
                    stack[-1][2] = True
                    stack[-1][0].left = node
                    
                # Otherwise, the current node is the right child
                # And since we found the left and right child of the node on top of stack
                # That node is no longer needed in the stack so we pop it as well
                else: stack.pop()[0].right = node
                    
            # Push current node the stack
            stack.append([node, depth, False])
        
        # Finally, return the root node of the tree
        return root
            
traversal = "1-2--3--4-5--6--7"

print("Output -> ", Solution().recoverFromPreorder(traversal))
            
                    
                    
            
            