class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encodes a list of strings to a single string.
        #Iterate through each string in the list
        #get length of each string        
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:              
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            decoded.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return decoded