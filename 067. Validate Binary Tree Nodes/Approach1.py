from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        
        # The root will not be the child of any node
        # So, first, we need to find the root node
        # Because, it is not necessary that the root will always be the node 0
        nodes = set()
        for i in range(n): nodes.add(i)
            
        for i in range(n):
            if leftChild[i] in nodes: nodes.remove(leftChild[i])
            if rightChild[i] in nodes: nodes.remove(rightChild[i])
                
        # At this point, there should be only one value in the set which is the root node
        # If the set is empty or has more than one nodes, then it means this is not a valid binary tree
        if not nodes or len(nodes) > 1: return False
        
        root = next(iter(nodes))
        
        # Now, we can simply traverse level-wise, starting from the root node
        queue = deque()
        queue.append(root)
        
        # To keep track of nodes that are already left or right child or some other node
        alreadyChildren = set()
        
        # How many nodes we traversed
        nodesTraversed = 0
        
        # While the queue is not empty
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Update the number of nodes traversed
            nodesTraversed += nodesInCurrentLevel
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front
                node = queue.popleft()
                
                # If the node has a left child
                if leftChild[node] > -1:
                    
                    # If this left child is already a child of some other node
                    # Then it means this is not a valid binary tree
                    if leftChild[node] in alreadyChildren: return False
                    
                    # Otherwise, add the node to the queue
                    queue.append(leftChild[node])
                    
                    # Add to the set
                    alreadyChildren.add(leftChild[node])
                    
                # If the node has a right child
                if rightChild[node] > -1: 
                    
                    # If this right child is already a child of some other node
                    # Then it means this is not a valid binary tree
                    if rightChild[node] in alreadyChildren: return False
                    
                    # Otherwise, add the node to the queue
                    queue.append(rightChild[node])
                    
                    # Add to the set
                    alreadyChildren.add(rightChild[node])
                
                # Update the count
                nodesInCurrentLevel -= 1
                
        # If the number of nodes we traversed is not n, then this is not a valid binary tree
        if nodesTraversed != n: return False
        
        # This is a valid Binary Tree
        return True

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]

print("Output -> ", Solution().validateBinaryTreeNodes(n, leftChild, rightChild))