class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # res = 0

        # for num in nums:
        #     res ^= num

        # return res

        # res = set()

        # for num in nums:
        #     if num not in res:
        #         res.add(num)
        #     else:
        #         res.remove(num)
        # return list(res)[0]
        

        
        res = {}

        for num in nums:
            if num not in res:                
                res[num] =  1
            else:
                del res[num]
        return list(res.keys())[0]