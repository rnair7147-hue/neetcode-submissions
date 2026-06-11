from typing import List

class Solution:
    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_number(token):
                stack.append(int(token))

            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num2 * num1)
                elif token == '/':
                    stack.append(int(num2 / num1))
        return stack.pop()