class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(set(prices))<2:
            return 0
        maxD = 0 
        minD = prices[0]

        for i in range(1,len(prices)):
            maxD = max(maxD , prices[i]-minD)
            minD = min(minD  , prices[i])
        return maxD
