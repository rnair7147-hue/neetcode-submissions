class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #If t is longer than s, return "" immediately.
        if len(t) > len(s):
            return ""

        #Build count_t frequency map for t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char,0) + 1

        # Window frequencies as we move
        window = {}  

        #Set need = len(count_t) and have = 0
        need = len(count_t)
        have = 0

        # Track the best answer bounds: [length, left_index, right_index]
        res = [float("inf"), -1, -1]

        left = 0
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Did this character just satisfy its required count?
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # While the window is valid, try to make it smaller!
            while have == need:
            # 1. Record the best answer so far
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right]
        
            # 2. Prepare to remove s[left] from the window
                left_char = s[left]
                window[left_char] -= 1
        
            # 3. Did removing this break our requirement?
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
            
            # 4. Move left forward
                left += 1
        
        l, r = res[1], res[2]
        return s[l : r + 1] if res[0] != float("inf") else ""    