class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Method to update the node values so that the tree follows Children Sum Property
    def updateTree(self, root, maxValue):

        # Base Case
        if not root: return

        # Update the maximum value
        maxValue[0] = max(maxValue[0], root.val)

        # If it is a leaf node, update its data to the maximum value in the Binary Tree
        if not root.left and not root.right: 
            root.val = maxValue[0]
            return

        # Traverse left
        self.updateTree(root.left, maxValue)

        # Traverse right
        self.updateTree(root.right, maxValue)

        # Check the condition
        left,right = 0,0
        if root.left: left = root.left.val
        if root.right: right = root.right.val

        # If root node's value is greater than sum of children node values
        if root.val > left + right:
            if left == 0: root.right.val = root.val
            elif right == 0: root.left.val = root.val
            elif root.left.val > root.right.val: root.right.val = root.val - root.left.val
            else: root.left.val = root.val - root.right.val
        # If root node's value is smaller than sum of children node values
        elif root.val < left + right: root.val = left + right

    def changeTree(self, root):
        
        # Maximum value in the tree
        maxValue = [0]

        # Call the function that updates the tree so that it follows children sum property
        self.updateTree(root,maxValue)


root = TreeNode(2)
root.left = TreeNode(35)
root.right = TreeNode(10)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(2)

Solution().changeTree(root)