class Solution:
    def isValid(self, s: str) -> bool:

        allowed = { '[':']', '(':')', '{':'}'}
        stack = []
        
        for char in s:
            if char in allowed:
                stack.append(char)
            else:
                if len(stack) > 0 and char == allowed[stack.pop()]:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
