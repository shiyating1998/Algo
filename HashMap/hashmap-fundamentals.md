# Hash Map Fundamentals

A **Hash Map** (or Hash Table) is a data structure that stores key-value pairs, offering efficient lookup, insertion, and deletion operations.

## Key Concepts
- **Hash Function**: Maps keys to indices in an underlying array. A good hash function minimizes collisions (different keys mapping to the same index).
- **Buckets**: Array elements where key-value pairs are stored. In case of collisions, each bucket may store multiple entries (via chaining or open addressing).
- **Load Factor**: Ratio of the number of stored elements to the total capacity. High load factors can decrease performance.

## Operations
1. **Insert(key, value)**:  
   - Compute hash of the key.  
   - Place the value in the corresponding bucket. Handle collisions if necessary.

2. **Get(key)**:  
   - Compute hash of the key.  
   - Retrieve the value from the corresponding bucket.

3. **Delete(key)**:  
   - Compute hash of the key.  
   - Remove the entry from the corresponding bucket.

## Advantages
- **O(1)** average time complexity for insert, search, and delete operations (with a good hash function).
- Useful for implementing caches, databases, and associative arrays.

## Disadvantages
- Performance degrades with poor hash functions or high collision rates.
- May require resizing and rehashing, which is costly in time.

## Best Practices
- Use a hash function that distributes keys uniformly.
- Monitor the load factor and resize the hash map dynamically.
- Handle collisions efficiently (e.g., separate chaining or linear probing).

## Common Use Cases
- Database indexing
- Caches (e.g., LRU Cache)
- Counting frequencies (e.g., word counts)
- Associative arrays and dictionaries in programming languages like Python (`dict`) or Java (`HashMap`)

### Collision in Hash Maps

A **collision** occurs when two different keys produce the same hash value and are assigned to the same bucket.

#### Collision Handling Strategies
1. **Separate Chaining**:  
   - Each bucket holds a list (or another data structure) of all key-value pairs mapping to that index.  
   - Lookup, insert, or delete operations traverse the list.

2. **Open Addressing**:  
   - Store all elements directly in the array by finding the next available slot (probing).  
   - Common probing methods:  
     - **Linear Probing**: Check the next bucket sequentially.  
     - **Quadratic Probing**: Use a quadratic function to determine the next bucket.  
     - **Double Hashing**: Use a second hash function for probing.

#### Impact of Collisions
- Increase the time complexity of operations from **O(1)** to **O(n)** in the worst case.
- Good hash functions and balanced load factors minimize collisions and ensure high efficiency.

#### Key Takeaway
Efficient collision handling is essential for maintaining the performance of a hash map.



### `defaultdict` Base Implementation: Time Complexity and Space Complexity

The `defaultdict` in Python is a specialized subclass of the built-in `dict`. It provides a default value for missing keys by using a factory function. Below, we analyze the base implementation, its underlying data structure, and the time and space complexities of its operations.

## Base Implementation of `defaultdict`
The `defaultdict` extends the `dict` class and uses a **hash table** internally for storing key-value pairs. It adds the feature of a **factory function** that is invoked when accessing a missing key.

### Key Components
1. **Hash Table**:
   - Like a regular dictionary, `defaultdict` uses a **hash table** to store keys and their associated values. 
   - The hash table consists of **buckets** where key-value pairs are stored, and each key is hashed to determine which bucket it belongs to.
   
2. **Factory Function**:
   - When a key is accessed that doesn't exist in the dictionary, the factory function (e.g., `int()`, `list()`, `set()`) is called to create a default value for that key.
   - The default value is inserted into the dictionary, and it is returned for the key.

### Example:
```python
from collections import defaultdict

# Default factory function is int, which returns 0 for missing keys
d = defaultdict(int)
d["a"] += 1  # "a" is missing, so defaultdict initializes d["a"] = 0, then increments it to 1
print(d)  # Output: {'a': 1}
