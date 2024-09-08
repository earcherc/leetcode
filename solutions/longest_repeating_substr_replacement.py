class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Ok this seems similar-ish to the last sliding window
        l = 0
        root = s[l]
        current = 0
        longest = 0
        replacements = k

        for r in range(len(s)):
            # if right pointer == root
            if s[r] == s[l]:
                current += 1
            elif s[r] != s[l] and replacements > 0:
                replacements -= 1
                r += 1
                current += 1
            elif s[r] != s[l] and replacements == 0:
                while s[l] == root:
                    l += 1
                replacements += 1
                current = r - l + 1

            if current > longest:
                longest = current

        return longest

        # This was my first attempt with some modifications
        # We got somewhat close and passed a few tests... but I don't think it's possible to fully solve this question like this
        # This question requires the hashmap counter that is used in the solution
        # How would we know this?
        # Well the main flaw is how do we keep track of replacements...
        # Ok so I guess in the previous problem we used a hashmap to check if we've seen a character
        # I guess hashmaps and sliding windows are well complimented
        
        # We shouldve first thought of WHAT MAKES A VALID WINDOW, not what to replace...
            # If possible we should have some condition/equation that we can check things against...
            # We are trying to MAXIMISE the window length
        # Window management is also crucial for these problems, what is the best way to update the window
