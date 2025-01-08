# Fundamentals of Binary Tree

## What is a Binary Tree?
A **Binary Tree** is a hierarchical data structure in which each node has at most two children, referred to as:
- **Left Child**
- **Right Child**

### Example of a Binary Tree:

---
    1
   / \
  2   3
 / \ / \
4  5 6  7

---

## Key Terminologies

1. **Node**: An element in the tree containing data and links to its children.
2. **Root**: The topmost node of the tree.
3. **Parent**: A node that has children.
4. **Child**: A node that has a parent.
5. **Leaf**: A node with no children.
6. **Height of a Tree**: The length of the longest path from the root to a leaf.
7. **Depth of a Node**: The length of the path from the root to that node.

---

## Types of Binary Trees

1. **Full Binary Tree**: Every node has either 0 or 2 children.
2. **Complete Binary Tree**: All levels are fully filled except possibly the last, which is filled from left to right.
3. **Perfect Binary Tree**: All internal nodes have 2 children, and all leaf nodes are at the same level.
4. **Skewed Binary Tree**: All nodes have only one child (left or right).
5. **Balanced Binary Tree**: The height difference between the left and right subtrees of every node is at most 1.

---

## Properties of Binary Trees

1. **Maximum Nodes** at height `h`:  
   \[
   2^h - 1
   \]

2. **Maximum Height** with `n` nodes (skewed tree):  
   \[
   n
   \]

3. **Minimum Height** with `n` nodes (perfect tree):  
   \[
   \log_2(n + 1)
   \]

4. **Number of Leaf Nodes** in a Full Binary Tree:  
   \[
   \frac{n + 1}{2}
   \]

---

## Binary Tree Traversals

### 1. **In-Order (Left, Root, Right)**  
Steps:
1. Traverse the left subtree.
2. Visit the root node.
3. Traverse the right subtree.

Example: `4 → 2 → 5 → 1 → 6 → 3 → 7`

---

### 2. **Pre-Order (Root, Left, Right)**  
Steps:
1. Visit the root node.
2. Traverse the left subtree.
3. Traverse the right subtree.

Example: `1 → 2 → 4 → 5 → 3 → 6 → 7`

---

### 3. **Post-Order (Left, Right, Root)**  
Steps:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root node.

Example: `4 → 5 → 2 → 6 → 7 → 3 → 1`

---

### 4. **Level-Order (Breadth-First)**  
Steps:
1. Visit nodes level by level from left to right.

Example: `1 → 2 → 3 → 4 → 5 → 6 → 7`

---

## Binary Tree Representation in Code

### Node Class (Python Example):
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Constructing the example binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
# In-Order Traversal
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)

in_order(root)  # Output: 4 2 5 1 6 3 7

Applications of Binary Trees
Expression Trees: Parsing and evaluating mathematical expressions.
Binary Search Trees: Fast lookup, insertion, and deletion.
Heap: Priority queues.
Huffman Trees: Data compression algorithms.
Red-Black Trees: Self-balancing binary search trees.
AVL Trees: Self-balancing binary search trees.
Splay Trees: Self-balancing binary search trees.
Scapegoat Trees: Self-balancing binary search trees.
B-Trees: Self-balancing binary search trees.