class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for elm in strs:
            sorted_string = "".join(sorted(elm)) 
            anagram_dict[sorted_string].append(elm)
            # if sorted_string in anagram_dict:
            #     #anagram_dict[sorted_string] = anagram_dict.get(sorted_string).append(str)
            #     #anagram_dict[sorted_string]=anagram_dict.setdefault(sorted_string, []).append(str)
            #     anagram_dict.get(sorted_string).append(str)
            # if sorted_string not in anagram_dict:
            #     anagram_dict[sorted_string] = []
            #     anagram_dict[sorted_string].append(elm)
            # else:
            #     anagram_dict[sorted_string] = elm
        return list(anagram_dict.values())


        


