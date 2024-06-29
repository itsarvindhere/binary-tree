class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        
        # A dictionary to keep track of nodes and their parents
        parents = {}
        
        # Iterate over all the node numbers
        for i in range(n):
            
            # A node cannot be the child of itself
            if leftChild[i] == i or rightChild[i] == i: return False
            
            # If the current node has a left child
            if leftChild[i] > -1: 
                
                # That left child should not have a second parent
                if leftChild[i] in parents: return False
                
                # It is not possible for a child to also be the parent of the same node
                if i in parents and parents[i] == leftChild[i]: return False
                
                # It is not possible that the "grandparent" of current node is same as its left child
                if i in parents and parents[i] in parents and parents[parents[i]] == leftChild[i]: return False
                
                # Update the dictionary
                parents[leftChild[i]] = i
            
            # If the current node has a right child
            if rightChild[i] > -1: 
                
                # That right child should not have a second parent
                if rightChild[i] in parents: return False
                
                # It is not possible for a child to also be the parent of the same node
                if i in parents and parents[i] == rightChild[i]: return False
                
                # It is not possible that the "grandparent" of current node is same as its right child
                if i in parents and parents[i] in parents and parents[parents[i]] == rightChild[i]: return False
                
                # Update the dictionary
                parents[rightChild[i]] = i
        
        # There must be only one node in a valid binary tree that does not have a parent (Root node)
        # It means, at this point, we should have "n - 1" entries in the dictionary if it is a valid tree
        if len(parents) != n - 1: return False
                
        # This is a valid Binary Tree
        return True

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]

print("Output -> ", Solution().validateBinaryTreeNodes(n, leftChild, rightChild))