class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        match = {"[":"]","{":"}","(":")"}
        lst = []
        while i < len(s):
            if s[i] in match:
                lst.append(match[s[i]])
            else:
                if not lst:
                    return False
                elif lst.pop() != s[i]:
                    return False
            i += 1
        if len(lst) > 0:
            return False      
        return True  