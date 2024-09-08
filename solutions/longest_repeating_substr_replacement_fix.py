class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # This solution will fix the mistakes made in the last attempt
        # So we need to keep track of how many replacements are being made
        # What is a valid window?
        # window length - most frequent character = replacements required
        # Replacements required must be less than or equal to k
        # So this means that with each window update, we are checking
        # whether we have enough replacements to make the window valid.
        # If we do not, then we need to move the left pointer (window) in
            # We check validity again
            # If we are valid we can move the right pointer forwards

        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:                
                count[s[r]] = 1
            
            windowLength = r - l + 1
            if windowLength - max(count.values()) <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                if not count[s[l]]:
                    del count[s[l]]
                l += 1
            
        return res
            
                
            



