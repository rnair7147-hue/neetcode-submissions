class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        final_lst = []
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        sorted_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
        for i,val in enumerate(sorted_dict):
            if i < k:
                final_lst.append(val)
            else:
                break
        return final_lst
            


