
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        char_freq = defaultdict(int)
        windowLength = 0
        maxWindow = 0
        while r < len(s):
            char_freq[s[r]] += 1 
            windowLength = r - l +1
            max_freq = max(char_freq.values())
            if (windowLength - max_freq) <= k:
                maxWindow = max(maxWindow, windowLength)
                r += 1                
            else:
                char_freq[s[l]] -= 1
                l += 1 
                r += 1               
        return maxWindow
        