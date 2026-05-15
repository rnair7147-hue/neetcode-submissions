# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         #pass
#         area = 0
        
#         for i in range(len(heights)):
#             counter = 1
#             for j in range (i + 1,len(heights)):                
#                 newarea = counter * min(heights[i], heights[j])
#                 area = max(area, newarea)
#                 counter += 1
#         return area  
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            area = max(area, (r-l) * min(heights[l] , heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1             

        return area