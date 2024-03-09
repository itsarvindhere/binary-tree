from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def binaryTreePath(self, root, val):
        
        # A queue
        queue = deque()

        # Initially, the queue will have the root node
        # The second value is the path till a node in the queue
        queue.append([root, [root.val]])

        # While the queue is not empty
        while queue:

            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)

            # While there are nodes in current level
            while nodesInCurrentLevel > 0:

                # Pop the node in front of the queue
                node, pathToItself = queue.popleft()

                # If this is the target node
                if node.val == val: 
                    # We are done
                    path = pathToItself
                    break
                
                # If the node has a left child, put it in the queue
                if node.left:
                    temp = pathToItself[:]
                    temp.append(node.left.val)
                    queue.append([node.left, temp])

                # If the node has a right child, put it in the queue
                if node.right:
                    temp = pathToItself[:]
                    temp.append(node.right.val)
                    queue.append([node.right, temp])

                # Decrement the count
                nodesInCurrentLevel -= 1
            
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