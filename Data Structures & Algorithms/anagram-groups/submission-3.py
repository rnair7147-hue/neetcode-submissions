class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for elm in strs:
            sorted_string = "".join(sorted(elm)) 
            anagram_dict[sorted_string].append(elm)

        return list(anagram_dict.values())


        


