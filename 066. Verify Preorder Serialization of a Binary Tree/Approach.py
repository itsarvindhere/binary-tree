class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        # Convert the string to a list
        preorder = preorder.split(",")
        
        # A Stack to efficiently iterate and keep track of the nodes
        stack = []
        
        # Index to iterate the list
        i = 0
        
        # Length
        n = len(preorder)
        
        while i < n:
            
            # If it is not the first node, and stack is already empty
            # Then it is not a valid serialzation
            if i > 0 and not stack: return False
            
            # If the stack is not empty
            if stack: 
                
                # If we have already visited the left child of previous node
                # Then it means the current node is the right child
                # And this means we visited both the children of previous node
                # So, we no longer have to keep track of it and so we can remove it
                if stack[-1]: stack.pop()
                    
                # Otherwise, it means the current node is the left child of the previous node
                else: stack[-1] = True
            
            # Push a flag to the stack that shows we are yet to find the left child of this node
            if preorder[i] != "#": stack.append(False)
                
            # Update the index
            i += 1
                      
        # This a valid serialization if the stack is empty
        return not stack

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"

print("Output -> ", Solution().isValidSerialization(preorder))