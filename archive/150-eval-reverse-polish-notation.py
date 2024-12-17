from typing import List

# Use a stack 
# O(n) time complexity, O(n) space 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c=='+' or c=='-' or c=='*' or c=='/':
                op2 = stack.pop()
                op1 = stack.pop()

                if c=='+':
                    stack.append(op1+op2)
                elif c=='-':
                    stack.append(op1-op2)
                elif c=='*':
                    stack.append(op1*op2)
                elif c=='/':
                    stack.append(int(op1/op2))  # truncate to zero int(op1/op2),  -0.4 ---> 0
                                                # op1//op2: floor division --->greatest integer <= result  -0.4 ---> -1
            else:
                stack.append(int(c))
        
        return stack.pop()                   

print(13/5)
print(13//5)
print(int(13/5))

print(6/-132)
print(6//-132)
print(int(6/-132))