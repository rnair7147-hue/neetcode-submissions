class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        itemList = {}

        for word in strs:
            count = [0] * 26  # one slot for each letter

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)  # lists can't be dict keys, tuples can

            if key not in itemList:
                itemList[key] = [word]
            else:
                itemList[key].append(word)

        return list(itemList.values())