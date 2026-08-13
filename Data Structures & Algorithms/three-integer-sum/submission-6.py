class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        nums.sort()
        for i,num1 in enumerate(nums):
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left ] + nums[right] < -num1:
                    left += 1
                    continue
                elif nums[left ] + nums[right] > -num1:  
                    right -= 1
                    continue
                else:
                    if ([num1, nums[left],nums[right]]) not in result:
                        result.append([num1, nums[left],nums[right]])
                    left += 1
                    right -= 1
        return result
                     


        
                    

            
