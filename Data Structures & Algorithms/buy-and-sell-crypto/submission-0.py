class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                diff = prices[j] - prices[i]
                if diff > 0:
                    maxprofit = max(maxprofit,diff)
        return maxprofit


        