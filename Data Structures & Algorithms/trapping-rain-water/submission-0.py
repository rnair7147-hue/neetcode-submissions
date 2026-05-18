class Solution:
    def trap(self, height: List[int]) -> int:
        #Find maxLeft
        # maxLeft =[]
        # for i in range(len(height)):
        #     maxLeft.append(i) = max(height[i+1],height[len(height) - 1])
        maxLeft =[0] * len(height)
        for i,num in enumerate(height):
            if i == 0:
                continue
            maxLeft[i] = max(maxLeft[i - 1],height[i -1])
        #Find maxRight
        maxRight =[0] * len(height)
        for i in range(len(height) - 1 , -1, -1):
            if i == len(height) - 1:
                continue
            maxRight[i] = max(maxRight[i + 1],height[i + 1])
        #Find min(l,r)
        minArray = [0] * len(height)
        for i in range(len(height)):
            minArray[i] = min(maxLeft[i],maxRight[i])
        #Find Trapped water area
        area = 0
        for i in range(len(height)):
            if((minArray[i] - height[i]) > 0):
                area += (minArray[i] - height[i])
        return area        
        