class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # I think this is our first hard attempt
        # This doesn't seem that bad, but there's probably some trick

        # two pointer/sliding window

        # case sensitive
        # doesn't have to be in order 
        # shortest substring possible, we've been dealing with maximum in last problems
        # what is a valid window then and what is the window update condition
        # valid window = the substring characters are within the window
            # how will we calculate this
            # we can count the frequencies
            # then do a loop over the substring to check if each char is in the window
            # if it isnt, then we continue to grow the window to the right
            # if it is, then we should try and minimise the window?
                # since this new iteration is valid, we should try moving the left pointer forwards while the condition remains...
                # if it is still valid and shorter, then we can update the shortest result

        # Is this it?
        # iterate over the string
            # check if valid
                # move right pointer if not
                # move left pointer while still valid

        if len(s) < len(t):
            return ""
        
        shortest = s
        l = 0
        count = {}

        def valid(l):
            sub_count = {}
            for char in t:
                if char in sub_count:
                    sub_count[char] += 1
                else:
                    sub_count[char] = 1

                if char not in count:
                    return False
                elif char in count and count[char] < 1:
                    return False
            
            # if s[l] is part of t and the count of s[l] is greater than count of s[l] in t
            # decrement and move to right
            if s[l] in sub_count and count[s[l]] > sub_count[s[l]]:
                return True
            
            return False

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            # Ok, so "AODBC" t="ABC"
            # We can't just move the left pointer in... it will destroy the validity
            # only move the left pointer in if removing it keeps it valid
            while valid(l) and l < r: 
                count[s[l]] -= 1
                l += 1
                substr = s[l:r + 1]
                if len(substr) < len(shortest):
                    shortest = substr
            
        return shortest
