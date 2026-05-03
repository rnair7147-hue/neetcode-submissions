class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        freq_elements = []
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] = num_dict.get(num) + 1
        num_dict_sorted = dict(sorted(num_dict.items(), key=lambda item: item[1],reverse=True))
        for i,(key,value) in enumerate(num_dict_sorted.items()):
            if i < k:
                freq_elements.append(key)
        return freq_elements



