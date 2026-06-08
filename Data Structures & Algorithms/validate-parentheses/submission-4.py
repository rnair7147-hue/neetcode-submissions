class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        valid_chars = {'(' : ')','{' : '}','[' : ']'}

        for char in s:
            if char in valid_chars:
                stack.append(char)
            elif len(stack) > 0 and char == valid_chars[stack[-1]]:
                    stack.pop()
            else:
                return False
        if len(stack) >  0:
            return False
        return True
        