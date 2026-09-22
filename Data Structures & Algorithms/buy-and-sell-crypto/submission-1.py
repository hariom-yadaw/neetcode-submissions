class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dayBuy, daySell = 0, 1
        maxProfit = 0

        while daySell < len(prices):

            if prices[daySell] > prices[dayBuy]:
                profit = prices[daySell] - prices[dayBuy]
                maxProfit = max(maxProfit, profit)
            else:
                dayBuy = daySell
                
            daySell += 1
        
        return maxProfit