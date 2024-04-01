class Solution:
    def maximumDifference(self, prices: List[int]) -> int:

        maxD =-1
        minD = math.inf

        for i in range(len(prices)):
            if i > 0 and prices[i]> minD:
                maxD = max(maxD , prices[i]-minD)
            minD = min(minD  , prices[i])
            
        return maxD