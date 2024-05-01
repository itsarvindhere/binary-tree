from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        
        # If the tree has no nodes
        if not root: return False
        
        # A Queue, initially with the root node and the target to find
        queue = deque()
        queue.append((root, targetSum))
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue along with the remaining target
                node, remainingTarget = queue.popleft()
                
                # If the remainingTarget is same as current node's value and this is a leaf node
                # It means we found one valid path
                if not node.left and not node.right and remainingTarget == node.val: return True
                
                # Otherwise, push left child and right child to the queue
                if node.left: queue.append((node.left, remainingTarget - node.val))
                if node.right: queue.append((node.right, remainingTarget - node.val))
                
                # Update the count
                nodesInCurrentLevel -= 1
                
        # There exists no path that satisfies the criteria
        return False

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print("Output ->", Solution().hasPathSum(root, 22))