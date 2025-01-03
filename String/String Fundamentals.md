# **Understanding Strings in Programming**

A **String** is a sequence of characters, often used to represent text in programming. Strings are a fundamental data type in most programming languages and play a crucial role in handling text-based data.

---

## **Key Properties of Strings**
1. **Immutable**: In many languages (e.g., Python, Java), strings are immutable, meaning they cannot be changed after creation. Modifications result in creating a new string.
2. **Zero-Based Indexing**: Strings are accessed using zero-based indexing, i.e., the first character is at index `0`.
3. **Character Set**: Strings consist of characters defined by encoding schemes like ASCII or Unicode.

---

## **Basic Operations**
### 1. **Concatenation**
Combining two or more strings.
```python
# Example in Python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
