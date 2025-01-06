# Algorithms and Leetcode Solutions (Python)

## 1. Understand the Problem
- **Clarify the input and output:**
  - Read the problem carefully and identify all constraints (e.g., data type, range, size).
  - Understand the desired relationship between input and output.
- **Ask questions (if applicable):**
  - What happens in edge cases like empty input, very large/small input, duplicates, etc.?
  - Are there time or space complexity requirements?

## 2. Simplify the Problem
- **Divide into subproblems:**
  - Break the problem into smaller, manageable chunks.
- **Use brute force (if needed):**
  - Start with a simple, naive solution to validate understanding before optimizing.
- **Focus on the core logic:**
  - Ignore edge cases temporarily to concentrate on solving the primary problem.

## 3. Generalize a Solution
- **Find patterns:**
  - Look for common patterns in how inputs map to outputs.
  - Think about how you would solve the problem manually.
- **Derive a generalized approach:**
  - Abstract your observations into a step-by-step algorithm.

## 4. Design the Algorithm
- **Choose the right data structures:**
  - Arrays, hash maps, heaps, stacks, etc., depending on the problem.
- **Write pseudocode:**
  - Plan the logic in a human-readable format before coding.

## 5. Implement the Solution
- Write clean, modular code with comments explaining key steps.
- Avoid over-complicating; stick to your plan.

## 6. Test Thoroughly
- **Test against all cases:**
  - Typical cases, edge cases, and constraints (e.g., very large inputs).
- **Use assertions:**
  - Assert conditions for expected outputs to confirm correctness.

## 7. Optimize
- Check the time and space complexity of your solution.
- Refactor if it can be made more efficient while preserving correctness.

## 8. Reflect and Learn
- If you missed any edge cases, analyze why.
- If your solution was suboptimal, explore other solutions (via discussions or hints).

---

## Example Workflow: Two Sum
### Problem Description
- **Input:** Array of integers and a target sum.
- **Output:** Indices of two numbers that add up to the target.
- **Constraints:** Each input has exactly one solution.

### Steps:
1. **Understand:**
   - Identify inputs like small arrays, large arrays, negative numbers, duplicates, etc.
2. **List Cases:**
   - Examples: `[1, 2, 3, 4]`, `[3, 3]`, `[0, 4, 3, 0]`.
3. **Generalize:**
   - Use a hash map to store indices of seen numbers and check for complements.
4. **Simplify:**
   - Start with a brute force solution using nested loops to verify the logic.
5. **Design:**
   - Implement an optimized solution using a hash map for O(n) time complexity.
6. **Implement:**
   - Write the code, ensuring clarity and modularity.
7. **Test:**
   - Test against all edge cases and constraints.
8. **Optimize:**
   - Ensure no redundant lookups; verify the efficiency of the hash map.
