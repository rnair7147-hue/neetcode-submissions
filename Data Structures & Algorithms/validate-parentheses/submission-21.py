class Solution:
    def isValid(self, s: str) -> bool:
        # i = 0
        # match = {"[":"]","{":"}","(":")"}
        # lst = []
        # while i < len(s):
        #     if s[i] in match:
        #         lst.append(match[s[i]])
        #     else:
        #         if not lst:
        #             return False
        #         elif lst.pop() != s[i]:
        #             return False
        #     i += 1
        # if len(lst) > 0:
        #     return False      
        # return True  

        valid_lst = {"(": ")", "{" : "}","[" : "]"}
        stack = []
        if len(s) <= 1:
            return False
        for c in s:
            if c in valid_lst:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if c != valid_lst[top]:
                        return False
        if len(stack) != 0:
            return False
        return True