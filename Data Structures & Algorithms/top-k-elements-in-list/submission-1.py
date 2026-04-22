class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        final_lst = []
        for num in nums:
            if num in num_dict:
                num_dict[num] = num_dict.get(num, 0) + 1
            else:
                num_dict[num] = 1
        sorted_dict = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)
        for i,(number, freq) in enumerate(sorted_dict):
            if i < k:
                final_lst.append(number)
            else:
                break
        return final_lst
    
            


