class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = { ')':'(' ,'}':'{',']':'['}

        for char in s:
            if char in map:
                if len(stack) > 0 and stack.pop() == map[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        return True
