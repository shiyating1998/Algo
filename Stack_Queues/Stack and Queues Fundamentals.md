# Stack and Queue: Data Structures

## Stack

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The element that is added last is the one to be removed first.

### Key Operations:
1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove the top element from the stack.
3. **Peek/Top**: View the top element without removing it.
4. **IsEmpty**: Check if the stack is empty.

### Real-World Examples:
- Undo operation in text editors.
- Backtracking problems like maze solving or function recursion.

### Visualization:
| Element 3 (Top) | | Element 2 | | Element 1 |

---

## Queue

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. The element that is added first is the one to be removed first.

### Key Operations:
1. **Enqueue**: Add an element to the end of the queue.
2. **Dequeue**: Remove the element from the front of the queue.
3. **Front/Peek**: View the element at the front without removing it.
4. **IsEmpty**: Check if the queue is empty.

### Types of Queues:
1. **Simple Queue**: Standard FIFO behavior.
2. **Circular Queue**: Connects the end of the queue back to the front for efficient memory usage.
3. **Priority Queue**: Elements are dequeued based on priority rather than order.
4. **Deque (Double-Ended Queue)**: Allows insertion and removal at both ends.

### Real-World Examples:
- Ticketing systems.
- Print job scheduling in printers.

### Visualization:
Front --> [Element 1] [Element 2] [Element 3] <-- Rear


---

## Key Differences Between Stack and Queue

| Feature         | Stack (LIFO)         | Queue (FIFO)        |
|------------------|----------------------|---------------------|
| Insertion/Removal | One end (Top)        | Two ends (Front & Rear) |
| Access Order     | Last in, First out   | First in, First out |
| Real-World Use   | Undo, Function Call  | Ticketing, Scheduling |

---

## Applications in Algorithms:
1. **Stacks**:
   - Depth-First Search (DFS).
   - Parsing expressions (e.g., postfix evaluation).
   - Balancing symbols (e.g., parentheses).

2. **Queues**:
   - Breadth-First Search (BFS).
   - Scheduling tasks.
   - Handling asynchronous data (e.g., I/O Buffers).

---
