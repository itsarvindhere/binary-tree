# PROBLEM STATEMENT

You are given a Node's value. Assume that the nodes in the Binary Tree have unique values. You need to print the path from the Root Node to the node with the given value.

![alt text](image.png)

Suppose we have a Binary Tree as above. If the node to which we have to reach is node {5}, then the Root to Node path will be - 

    1->2->3

So, we have to return a list with comma separated node values which denote the path from root to node.

For above Binary Tree, the output is - 

    [1,2,3]

# APPROACH

We will use the Pre-Order Traversal in this problem, the reason being that it is the simplest of the three to implement. We can do it using other two traversals in DFS, but that will make the code a bit more complicated.

![alt text](image-1.png)

Let's take the above example where we have to find the node with value = 7.

We start with the Root Node because remember it is the "Root -> Left -> Right" traversal. We see that root node has a value = 1 so it is not the node that we want to reach. But, it might be the node in the path to the target node so, we will save its value in a list. Path becomes [1]

Now, we traverse the left side of the root node.

We reach Node 2. Again, same logic. Path becomes [1,2]

We traverse the left of Node 2. Same logic. Path becomes [1,2,4]

Now, there is nothing on the left of Node 4. What does it mean? It means that the target node "7" is definitely not on the left side of "4". So, when we traverse the left of 4, that traversal will return False which represents that on the left of 4, we cannot find node 7.

Now, as per Pre-Order traversal, we now check the right side of "4". Again we see that there is nothing on right side and the right side traversal also returns False.

And so, when we are at the node "4", both left and right traversals give us False. So, node "7" is neither on left or on right side of node 4.

What does this mean? It means, the node "4" can never be in the path to the target node. So, we will remove "4" from the path list. Path list becomes [1,2].

And we again reach the node "2" and now, its time to traverse right side of "2" because we know on left, the target node cannot be present.

We reach node 5. We put it in the path list. Path list becomes [1,2,5]

Now we traverse left of 5 and reach 6. We put 6 in the path list. Path list becomes [1,2,5,6]

Now, on left of "6", there is nothing and also on right. So here as well, both the left and right traversals will give us False. It means, "6" cannot be in the path from root to node 7. So, it should be removed from the list.
Path list becomes [1,2,5]

Now, we traverse right side of "5". We reach the node 7. We see that this is the node to which we had to reach. And so, we will put it in the Path list and we know that the path is now found. There is no need to traverse left or right of 7 because we reached the target node. So, we can return True. 

So, when we are at the node "5", the left traversal gives us False but right traversal gives us True. It means "5" is definitely in the path from Root to Node so it should not be removed from the Path List.

Similarly, when we are at the node "2", the left traversal gives False but right traversal gives True. It means "2" is definitely in the path from Root to Node so it should not be removed from the Path List.

Finally, when we are at the Node "1", we see that the left traversal gives us True so it means there is no need to even traverse on right side because we already know that left side has the target node.

So, the recursive function ends.

And finally, the path list we get is - 

    [1,2,5,7]

And that's the whole idea.

So, here are the key points - 

1. When we reach the leaf node and it is not the target node, we know this path does not have the target node so we return False

2. If left traversal returns True, it means the target node is on left side of current root node so no need to traverse right side.

3. If none of the left or right traversals give us True, it means the target node is not on current path so the root node needs to be removed from the path list and we return False.

