class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # So this is a two pointer, I almost forgot
        # Why does it seem like a two pointer?
            # Height x Width, we need to keep track of two things at once
        # Ok so we need to find the largest volume
        # We find this by Height x Width
        
        # With two pointer solutions we definitely need to sort, but we also need to keep track of index
        # This is tough
        # Brute force solution
        # We need to calculate for each pair 
            # absolute difference in index * minimum height
            # n^2 solution

        # Okay so we couldn't figure out the pointer logic with this problem
        # The pointers were at the start and end
        # The condition to move a pointer was dependent on which was smaller
        # At each step we calculate the area

        def volume(l, r):
            height = min(heights[l], heights[r])
            width = r - l
            return height * width

        max_area = 0

        l, r = 0, len(heights) - 1
        while l < r:
            area = volume(l, r)

            if area > max_area:
                max_area = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

            
