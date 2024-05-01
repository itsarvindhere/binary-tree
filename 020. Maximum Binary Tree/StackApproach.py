
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        
        # Length of the list
        n = len(nums)
        
        # A Stack
        stack = []
        
        # Iterate over the list from left to right
        for num in nums:
            
            # New Node
            node = TreeNode(num)
            
            # Last Node Popped from stack
            lastNodePopped = None
            
            # First, remove all the nodes that have a smaller value than "node"
            while stack and stack[-1].val < node.val: 
                lastNodePopped = stack.pop()
                
            # Now, we can push "node"
            # If the stack is not empty
            # It means, "node" will be the right child of the node on top of stack
            if stack: stack[-1].right = node
                
            # What about the nodes we popped?
            # Those will now be part of "left" subtree of the "node"
            if lastNodePopped: node.left = lastNodePopped
                
            # Push the node to the stack
            stack.append(node)
            
        # Finally, we return the root node, which is the node at the bottom of the stack
        return stack[0] 


nums = [3,2,1,6,0,5]

print("Output -> ",Solution().constructMaximumBinaryTree(nums))