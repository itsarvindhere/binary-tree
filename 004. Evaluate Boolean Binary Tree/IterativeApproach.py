# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def evaluateTree(self, root):

        # Stack, initialy with the root node
        stack = [root]

        # While the stack is not empty
        while stack:

            # Node on top of the stack
            node = stack.pop()

            # If this is not a leaf node, then it will have a value 2 or 3
            if node.val > 1:

                # If the nodes on left and right are leaf nodes
                # That is, their values are 0 or 1
                if node.left.val < 2 and node.right.val < 2:

                    # Update the value of the root node
                    node.val = (node.left.val or node.right.val) if node.val == 2 else (node.left.val and node.right.val)

                # Otherwise, if at least one node on the left or right is having a value 2 or 3
                else:

                    # Push the root node back in the stack
                    stack.append(node)

                    # If the right child has a value 2 or 3, put it in the stack
                    if node.right.val > 1: stack.append(node.right)

                    # If the left child has a value 2 or 3, put it in the stack
                    if node.left.val > 1: stack.append(node.left)

        # If the root node's value at the end is 1, then it means the overall result is "True", else it is "False"
        return root.val == 1

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print("Output -> ", Solution().evaluateTree(root))