class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = [[]]
        # for num in nums:
        #     new_subsets = []
        #     for subset in result:
        #         new_subsets.append(subset + [num]) 
        #     result += new_subsets
        # return result

        result = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                result.append(curr.copy())
                return
             
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
            
        dfs(0)
        return result