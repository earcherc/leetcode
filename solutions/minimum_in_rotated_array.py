class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Ok this isn't that complicated
        # If we know how to do the binary search we can do this
        # The array is sorted, but its just offset
        # So our binary search will operate a little differently
        # We need to find the minimum value
        # In a sorted array the minimum would be the leftmost value 
        # So now if we get the midpoint, what info can we get out of this
        # well if the left most pointer is less than the midpoint
        # we know the entire left side of the array is sorted...
        # this automatically means that to the right of the midpoint
        # this is not ordered, and thus, our minimum value lies there
        # if the left pointer is larger than the midpoint
        # that means that somewhere to the left of the array, we have the beginning
        # and thus, we have the minimum somewhere on the left side

        # so clearly this is a modified binary search... 
        # the difference is that we are trying to find where the start of the array is
        # instead of a target
        # we also don't know what the minimum is

        def mbs(arr, l=0, r=None):
            if r is None:
                r = len(arr) - 1
            
            if l == r:
                return arr[l]

            mid = (l + r) // 2

            # If the middle element is greater than the rightmost element,
            # the minimum is in the right half
            if arr[mid] > arr[r]:
                return mbs(arr, mid + 1, r)
            # If the middle element is less than or equal to the rightmost element,
            # the minimum is in the left half or at mid
            else:
                return mbs(arr, l, mid)

        return mbs(nums)


