class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for elm in strs:
            # sorted_string = "".join(sorted(elm)) 
            # anagram_dict[sorted_string].append(elm)
            count = [0] * 26
            for c in elm:
                count[ord(c) -ord('a')] += 1
            anagram_dict[tuple(count)].append(elm)

        return list(anagram_dict.values())


        


