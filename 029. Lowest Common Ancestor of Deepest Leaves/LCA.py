from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Pre Order Traversal to find the lowest common ancestor of two nodes
    def preOrder(self, root, p, q, lca):
        
        # If node is Null or node is p or node is q
        # We will return the node itself
        if not root or root == p or root == q: return root
        
        # Otherwise, check on left if we have p or q
        nodeMatchedOnLeft = self.preOrder(root.left, p, q, lca)
        
        # Check on Right if we have p or q
        nodeMatchedOnRight = self.preOrder(root.right, p, q, lca)
        
        # If there is "p" or "q" on left and also on right
        # It means the current "root" is the lowest common ancestor of these nodes
        if nodeMatchedOnLeft and nodeMatchedOnRight: lca[0] = root
            
        # Otherwise, if there is "p" or "q" on one side but not on the other
        # Then it means the lowest common ancestor will be the node found on that side
        else: lca[0] = nodeMatchedOnLeft or nodeMatchedOnRight
        
        # Return the lowest common Ancestor 
        # This return value is going to be used as the result of current call, 
        # in previous calls of this recursive function
        return lca[0]
    
    
    def lcaDeepestLeaves(self, root): 
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # First and last nodes in each level
        first, last = root, root
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # A flag for the first node
            firstNodeFound = False
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If flag is false, this is the first node
                if not firstNodeFound: 
                    first = node
                    firstNodeFound = True
                
                # Update the last node. In this way, at the end, "last" will point to the last node of this level
                last = node
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
        # Finally, return the lowest common Ancestor by calling the helper function
        lca = [root]
        self.preOrder(root, first, last, lca)
        
        return lca[0]
                
                
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(Solution().lcaDeepestLeaves(root))