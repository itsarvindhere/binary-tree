# PROBLEM STATEMENT

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# EXAMPLE

![alt text](image.png)

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]

Output: [3,9,20,null,null,15,7]

# APPROACH

The idea is exactly the same as the problem "Construct Binary Tree from Preorder and Inorder Traversal".

In this problem, the only difference is that since "Post Order" traversal is "Left -> Right -> Root", at any time, the root node will be the node at "postEnd" index, not at the "postStart" index.

And so, we have to update the indices accordingly when we make the recursive calls.