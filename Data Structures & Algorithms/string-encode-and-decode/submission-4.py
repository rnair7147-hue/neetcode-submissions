class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr =''
        for s in strs:
            encodedStr += str(len(s)) + '#' + s
        return encodedStr
        
    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0
        lengthOfStr = ''
        if len(s) == 2:
            return ['']
        while i < len(s) -1 :
            while (s[i].isdigit() and s[i + 1] == '#') or (s[i].isdigit() and s[i + 1].isdigit()):
                if i >= len(s) - 1:
                    break
                lengthOfStr += s[i]
                i += 1 
                index = s.find('#', i, len(s))
                subString = s[i : index]
                # if index == -1:
                #     break
                
            length = int(lengthOfStr)
            decodedStrs.append(s[i+1 : i+length+1])
            i = i + length + 1
            lengthOfStr = ''
        return decodedStrs    


