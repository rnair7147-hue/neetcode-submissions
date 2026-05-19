class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        substr = ""
        maxlength = 0
        while r < len(s):
            if s[r] not in substr:
                substr += s[r]                
                r += 1 
            else:
                #find the position of first occurence of duplicate element
                indexFound = s[l:r].find(s[r])                
                l = l+indexFound + 1  
                r = r+1        
                substr = s[l:r]
                
            maxlength = max(maxlength, len(substr))
        return maxlength