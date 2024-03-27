# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def inorderTraversal(self, root):
        
        # In Order Traversal Result
        inorder = []
        
        # A Pointer, initially pointing to root node
        node = root

        # While the pointer is not null
        while node:

           # CASE 1 - NO LEFT SUBTREE
            if not node.left:

                # Put the value in the inorder list
                inorder.append(node.val)

                # Move towards right
                node = node.right

            # If there is a left subtree
            else:

                # Find the rightmost node in this left subtree
                # Because in the In Order Traversal, that node will be visited at the very end of this left subtree's traversal
                temp = node.left

                # Go to the rightmost node
                # And we also want to make sure there is no thread already
                while temp.right and temp.right != node: temp = temp.right

                # If the rightmost node has Null on its right (Which should be the case if there is no Thread already)
                if not temp.right:

                    # Add the thread
                    temp.right = node

                    # Now, move to the left subtree
                    node = node.left
                
                # CASE 2 - THREAD ALREADY EXISTS
                # If right child is not null
                # It means, the loop ended because rightmost node has a thread already
                else:

                    # So, we have to remove this thread
                    temp.right = None

                    # Put the root node's value in the inorder list
                    inorder.append(node.val)

                    # And now we move to the right subree
                    node = node.right

        # Finally, return the In Order Traversal result
        return inorder


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
root.right = TreeNode(3)

print("In Order Traversal -> ", Solution().inorderTraversal(root))