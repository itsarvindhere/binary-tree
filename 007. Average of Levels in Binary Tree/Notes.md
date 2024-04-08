# PROBLEM STATEMENT

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# EXAMPLE

![alt text](image.png)

Output: [3.00000,14.50000,11.00000]

Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.

Hence return [3, 14.5, 11].

# APPROACH

Since all we want is the average of all the nodes in each level, it makes sense to do a Level Order Traversal of the tree.