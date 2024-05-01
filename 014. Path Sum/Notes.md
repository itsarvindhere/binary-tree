# PROBLEM STATEMENT

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

# EXAMPLE

![alt text](image.png)

Input: targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

# APPROACH

The basic idea is that at each node, we are keeping track of how much remaining sum we have left to find on this current path. And if we are at a leaf node and the remaining sum is same as the leaf node's value, it basically means from root to this leaf node, we have a path sum equal to the targetSum.

