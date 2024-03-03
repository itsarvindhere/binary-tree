# PROBLEM STATEMENT

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

![alt text](image.png)

Output: [1,3,4]

# BFS APPROACH

The approach is pretty simple. The right side view means the rightmost node in each level. So, we can use Level Order Traversal here and as we go over each level, we know that the last node we traverse in each level is the rightmost node for that level. So, that's the whole approach.

# DFS APPROACH

The DFS Approach requires us to keep track of each level and we also have to use a Dictionary to keep track of each level and the rightmost node in that level.

At the end, we have to construct the final output list.