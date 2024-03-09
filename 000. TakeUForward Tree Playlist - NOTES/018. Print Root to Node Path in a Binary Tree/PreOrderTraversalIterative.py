# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def binaryTreePath(self, root, val):
        
        # Path
        path = []
            
        # A Stack, initially with the root node
        stack = [root]

        # While the stack is not empty
        while stack:

            # Pop the node on top of the stack
            node = stack.pop()

            # Push the node to the path so far
            path.append(node)

            # If this is the node we want
            if node.val == val: break

            # If the current node is a leaf node
            # It means at current path, we do not have the desired node, so, pop the current node from path
            if not node.left and not node.right: 
                path.pop()

                # We will now remove all the nodes in the current path so far that are no longer useful
                # Suppose current node "x" is a leaf node
                # And we remove it
                # Now, the parent node "y" may or may not be useful anymore
                # For example, if the parent node "y" had a right node as "x", it means we are done traversing left and right of "y" and we did not find a node with value = val on either side. So, "y" should be popped as well
                # Or if parent node "y" has only one child on left as "x", then also the same case
                # And similarly, we will check the same for the node that is the parent of "y" and so on...
                temp = node
                while path and (path[-1].right == temp or (not path[-1].right and path[-1].left == temp)): 
                    temp = path.pop()
                    
            # If the node has a right child, push to the stack
            if node.right: stack.append(node.right)

            # If the node has a left child, push to the stack
            if node.left: stack.append(node.left)

        path = [node.val for node in path]
            
        # Return the path
        return path


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right = TreeNode(3)

val = 7

print("Path is ->", Solution().binaryTreePath(root,val))