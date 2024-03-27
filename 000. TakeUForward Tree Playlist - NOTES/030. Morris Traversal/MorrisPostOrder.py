# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def postorderTraversal(self, root):
        
        # Post Order Traversal Result
        postorder = []
        
        # A Pointer, initially pointing to root node
        node = root

        # While the pointer is not null
        while node:

           # CASE 1 - NO RIGHT SUBTREE
            if not node.right:

                # Put the node value in postorder list
                postorder.append(node.val)

                # Move towards left
                node = node.left

            # If there is a right subtree
            else:

                # Find the leftmost node in this right subtree
                # Because in the Post Order Traversal, that node will be visited at the very end of this right subtree's traversal
                temp = node.right

                # Go to the left node
                # And we also want to make sure there is no thread already
                while temp.left and temp.left != node: temp = temp.left

                # If the leftmost node has Null on its left (Which should be the case if there is no Thread already)
                if not temp.left:

                    # Put the node value in postorder list
                    postorder.append(node.val)

                    # Add the thread
                    temp.left = node

                    # Now, move to the right subtree
                    node = node.right
                
                # CASE 2 - THREAD ALREADY EXISTS
                # If left child is not null
                # It means, the loop ended because leftmost node has a thread already
                else:

                    # So, we have to remove this thread
                    temp.left = None

                    # And now we move to the left subree
                    node = node.left

        # Finally, return the Post Order Traversal result by reversing the list
        postorder.reverse()
        return postorder


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
root.right = TreeNode(3)

print("Post Order Traversal -> ", Solution().postorderTraversal(root))