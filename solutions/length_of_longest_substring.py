class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # This seems more like a classical sliding window problem
         # I guess the optimal solution would solve this in O(n)
         # I guess we will have a left pointer that starts the sequence
         # if the next item is the next asci value, we move the right pointer forwards
         # if the next asci value is not sequential, we update the max length

        # Okay we tried a simple solution but quickly realised again that it needs sliding window
        longest = 0
        seen = {}
        l = 0
        
        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]]
                l += 1

            seen[s[r]] = 1
            longest = max(longest, r - l + 1)
            
        return longest


