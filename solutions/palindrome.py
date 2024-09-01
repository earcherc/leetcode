class Solution:
    def isPalindrome(self, s: str) -> bool:
        # What is the solution to this
        # It must involve two pointers, we know that
        # If we could filter the string and remove all non alphanumeric chars, we would have a string we can search
        # We would then iterate the pointers from the start and end, checking that they match with each iteration
        # If the pointers cross eachother, we know we were succesful
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())

        left_idx = 0
        right_idx = len(s) - 1

        if len(s) == 1:
            if s.isalpha():
                return True

        while left_idx < right_idx:
            if s[left_idx] == s[right_idx]:
                left_idx += 1
                right_idx -= 1
            else:
                return False
        
        return True

