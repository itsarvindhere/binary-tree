# PROBLEM STATEMENT

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# EXAMPLE

![alt text](image.png)

preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Output: [3,9,20,null,null,15,7]

# APPROACH

Basically, the idea is that if we are given the In Order traversal of a tree and one of Pre Order or Post Order traversals, then we can certainly create a "UNIQUE" binary tree.  There is a reason for this.

We know that "In Order" Traversal follows "Left -> Root -> Right" approach when traversing the tree. In other words, it first traverses the left subtree, then the root and then the right subtree.

On the other hand, the "Pre Order" traversal follows the "Root -> Left -> Right" approach. In other words, it first traverses the root, and then the left subtree and the right subtree.

How can this information be useful in this problem?

![image](https://assets.leetcode.com/users/images/eed83a9a-6fb1-4160-9356-17d2f450da62_1711272380.1416874.png)

	preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
	
	Let's say we are given the above preorder and inorder lists.
	
	Because preorder follows "root -> left -> right", 
	it is not hard to figure out that "3" is the root node's value for the final tree, right?
	
	Now, we see that in the inorder list, "3" is at an index 1.
	
	Remember that inorder traversal is "Left -> Root -> Right".
	
	So, if we know that "3" is the root node, and "3" is at index 1 in inorder list,
	
	We can say that whatever comes before "3" in inorder list is part of the left subtree.
	And whatever comes after "3" in inorder list is the part of right subtree.
	
	So, [9] is inorder traversal of left subtree and [15,20,7] is inorder traversal of right subtree
	
	Similarly, we can say 
	
	[9] is preorder traversal of left subtree and [20,15,7] is preorder traversal of right subtree
	
	So, at this point, we know that for left subtree -
	
		preorder = [9] and inorder = [9]
		
	And for right subtree, 
	
		preorder = [20,15,7] and inorder = [15,20,7]
		
	So, we can built the left and right subtrees and then simply attach them to the root node.
	
	So, we started with preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
	
	And then, we divided this problem into two subproblems.
	
	That is, we first build left subtree and then we build right subtree.
	
	So, that's the logic we will follow in our recursive build function.
	
But, how to keep track of the sizes of preorder and inorder lists for each subtree? One way can be that, in every iteration, we will iterate over the inorder list to find at what index the current root's value is, then we get the left sublist, and then right sublist, and so on. And then we also divide the preorder list for both left and right subtrees. But, that would not be an efficient solution and may give TLE in some test cases.

An efficient approach is to take the indices of values in the original inorder list and save them in a Dictionary / Hash Table. And instead of dividing lists into sublists in each recursive call, we can simply use two pointers "start" and "end" for preorder and inorder lists that will tell us that the portion between [start,end] in preorder is the preorder traversal of current subtree, and the same for inorder traversal.

Let's see how that will work using the above example.

	preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
	
	indices = {9: 0, 3: 1, 15: 2, 20: 3, 7 : 4}
	
	Let's say preStart and preEnd are start and end pointers for preorder list
	Similarly, inStart and inEnd are start and end pointers for inorder list
	
	So, initially, preStart = 0, preEnd = 4, inStart = 0, inEnd = 4
	
	At any time, node at index "preStart" in preorder list will be root node of current subtree.
	
	So, initially root node is "3".
	
	Now, we check at what index "3" is present in inorder list. For that, we use our dictionary.
	
	We see that "3" is present at index "1" in inorder list.
	
	So, when we divide this inorder list into two parts for left and right subtrees,
	left part will have how many elements?
	
	That would simply be "index of 3 in inorder list - inStart"
	
	That is, 1 - 0 => 1
	
	And indeed we can see that there is only one element "9" on left of "3" in inorder list.
	
	So now, we can recursively call the build function for left and right subtrees.
	
	For the left subtree, the preorder list will be [9]
	
	It means, preStart will become 1,
	and preEnd will become "preStart + count of elements on left of 3 in inorder list"
	
	Similarly, for right subtree, preorder list will be [20,15,7]
	It means, preStart will become "preStart + count of elements on left of 3 in inorder list + 1"
	And preEnd will remain the same. That is "4"
	
	For the left subtree, the inorder list will be [9]
	That is, inStart will be the same => 0
	but, inEnd will become the "index of value 3 (root) in inorder - 1"
	
	For right subtree, the inorder list will be [15,20,7]
	So, inStart will be "index of value 3 (root) in inorder + 1"
	And inEnd remains the same. That is "4"
	
And that's how these pointers will help us in dividing the lists for left and right subtrees, without actually splitting the input lists into sublists.

And that's the whole approach!
class Solution:
    
    # Recursive Function to build the tree
    def build(self, preorder, inorder, preStart, preEnd, inStart, inEnd, indices):
        
        # Base Case
        # If there are no more nodes, return a Null node
        if preStart > preEnd or inStart > inEnd: return None
        
        # The value at the "preStart" index in preOrder list is the value of the root node of current tree
        root = TreeNode(preorder[preStart])
        
        # Now, before we recursively call the function for left and right subtrees
        # We need to find how many elements are there in inorder list for the left subtree
        # The inorder for left subtree will be values from index "inStart" to the index of "root" value in inorder (excluding itself)
        leftCount = indices[preorder[preStart]] - inStart
        
        # Now, build the left and right subtrees
        root.left = self.build(preorder, inorder, preStart + 1, preEnd + leftCount, inStart, indices[preorder[preStart]] - 1,indices)
        root.right = self.build(preorder, inorder, preStart + leftCount + 1, preEnd, indices[preorder[preStart]] + 1, inEnd,indices)
        
        # Return the root node of the tree
        return root
        
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Number of nodes
        n = len(inorder)
        
        # A Map to keep track of the indices of node values in "inOrder" list
        indices = {}
        for i in range(n): indices[inorder[i]] = i
            
        # Call the function to build the three which will return the tree after building it
        # Note that we are also passing the start and end indices of both the preorder and inorder lists
        # That's because, when we recursively call this function inside itself,
        # We will pass only a part of preorder and inorder lists in those calls
        # So, we don't want to lose track of the original indices 
        # since our "indices" dictionary only has original indices in it
        return self.build(preorder, inorder, 0, n - 1, 0, n - 1, indices)
```