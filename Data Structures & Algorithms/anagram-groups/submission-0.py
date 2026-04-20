class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        itemList ={}
        for i,item in enumerate(strs):
            result = "".join(sorted(item))
            if result not in itemList:
                itemList[result]= [item]
            else:
                itemList[result].append(item)
        res = [v for k, v in itemList.items()]
        return res