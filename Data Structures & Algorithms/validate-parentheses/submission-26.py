class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False

        allowed = {']' : '[',
                ')' : '(','}' : '{'}
        stack = []
        for bracket in s:
            if bracket in allowed.values():
                stack.append(bracket)
            elif bracket in allowed and len(stack) != 0:
                if allowed[bracket] != stack.pop():
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True

        