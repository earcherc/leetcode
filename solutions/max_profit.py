class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # So we know this is a sliding window problem
        # But how can we tell?

        # Solution
        # I think we have to iterate over the array and calculate each of the possible steps
        # So the smallest window is 2
        # We the next largest window is 3
        # All the way up until n
        # We need a double loop for this I guess
        # The outer loop dictates the window size
        # the inner loop iterates over and calculates each trade

        max_prof = 0
        for i in range(1, len(prices)):
            l,r = 0, i
            while r <= len(prices) - 1:
                profit = prices[r] - prices[l]
                if profit >= max_prof:
                    max_prof = profit
                l += 1
                r += 1
        
        return max_prof

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
