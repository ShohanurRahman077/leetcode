class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        for x in range(length):
            found = False

            for y in range(x+1,length):
                if prices[x]>= prices[y]:
                    prices[x]-=prices[y]
                    break
                    
            
        return (prices)