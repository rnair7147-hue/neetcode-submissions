class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #pass
        area = 0
        
        for i in range(len(heights)):
            counter = 1
            for j in range (i + 1,len(heights)):                
                newarea = counter * min(heights[i], heights[j])
                area = max(area, newarea)
                counter += 1
        return area    