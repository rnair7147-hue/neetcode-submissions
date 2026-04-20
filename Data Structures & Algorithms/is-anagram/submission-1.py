class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = []
        t_lst = []
        for char in s:
            s_lst.append(char)
        for char in t:
            t_lst.append(char)

        s_lst.sort()
        t_lst.sort()

        return s_lst == t_lst
         