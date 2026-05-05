class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        num_list = set()
        max_length = 0
        s_nums = sorted(nums)        
        for i,num in enumerate(s_nums):
                
            if i <= len(s_nums) - 2:
                if s_nums[i] + 1 == s_nums[i + 1]:
                    num_list.add(num)
                    num_list.add(num + 1)
                    i = i + 2
                elif s_nums[i] == s_nums[i + 1]:
                    num_list.add(num)
                    continue
                else:
                    max_length = max(max_length,len(num_list))
                    num_list.clear()
                    num_list.add(s_nums[i + 1])

        return max(max_length,len(num_list))

