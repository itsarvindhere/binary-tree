# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Helper function to traverse the tree and get the camera count
    def dfs(self, root, parent, grandParent, cameras, alreadyMonitored):
        
        # Base Case
        if not root: return
        
        # Traverse left
        self.dfs(root.left, root, parent, cameras, alreadyMonitored)
        
        # Traverse right
        self.dfs(root.right, root, parent, cameras, alreadyMonitored)
        
        # If the current node is not being monitored yet
        if root not in alreadyMonitored:
            
            # Add a camera to monitor it (This camera will either be added at this node itself or its parent)
            cameras[0] += 1
            
            # If there is a parent, then we should add a camera at the parent node
            if parent:
                
                # If we add a camera at the parent node,
                # The left, right and top nodes of the "parent" will all be monitored by this camera
                if parent.left: alreadyMonitored.add(parent.left)
                if parent.right: alreadyMonitored.add(parent.right)
                if grandParent: alreadyMonitored.add(grandParent)
                alreadyMonitored.add(parent)
        
    
    def minCameraCover(self, root):
        
        # If there is a single node
        if not root.left and not root.right: return 1
        
        # A set to keep track of the nodes that are already being monitored by the cameras
        alreadyMonitored = set()
        
        # Count of cameras
        cameras = [0]
        
        # Call the function to get the camera count
        self.dfs(root, None, None, cameras, alreadyMonitored)
        
        # Return the camera count
        return cameras[0]
        
root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)

print("Output -> ", Solution().minCameraCover(root))