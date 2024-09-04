class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This is a pretty interesting problem
        # Is it possible to use 3 pointers...
        # We need to find 3 numers that sum to 0
        # we need to create a new array of length 3
        # We start three pointers from index 0,1 and 2
        # we check if these == 0
            # if they do, we add this to an array
            # we then move each pointer to the right by two
        # if they don't == 0
            # we need to move one pointer over


        # Ok I don't think this solution really works
        # Thinking back to two pointer, I think we used a hashmap?
        # first we hash all the values and their index within the array
        # the we start two pointers that move over the array
        # we have a simple equation
        # a + b + c = 0
        # our two pointers will be aware of a and b, we just need to do an instant lookup for a value c that satisfies the equation
        # so, the pointers start and index 0 and 1
        # we get the sum of these e.g. -1 and 2
            # c = - a - b, so we need -(-1) - 2 = -1
            # we do an instant lookup in our hashmap for this value
            # if it exists, we take the 3 values, and append to an outer array
            # if it doens't exist, we move the second pointer to the right and try again


        # So we've completed two sum
        # That gives me a pretty good idea on how to solve this
        # We need the two pointers and to lookup the missing value with each pointer iteraiton
        # question is, how do we iterate the pointers
        # with a nested for loop it would be simple
        # how can we do it with two pointers
        # possible variations 
            # pointer at start and finish
            # I don't really understand how this would be different to nested for loop
            # we just going to check solution
        
        # Ok... so if we had done Two Sum 2, we would've realised that the pointers only really work
        # when the array is sorted. This is because we can perform a calculation on which pointer to shift
            # this was the key we were missing
            # It also means we don't need the hashmap it, the pointers are our counting mechanism
        # We then need to check all permutations of `a + b + c = 0`
        # if we handle `a`, the remaining problem is reduced to the two sum II pointer problem
        # so our outer loop iterates through the nums list
            # we need to check that as we iterate through, we skip duplicate values for the outer loop condiiton
            # our inner loop handles the two sum II logic
                # we need to start pointers at start and end of array
                # we have 3 conditions:
                    # the threeSum is too big, too small, or equal
                        # decrement right counter, increment left counter, or
                            # append the value to results
                                # we have to be careful bc 
        
        # let's learn how to implement quickosort
        # it's sort of fitting because it is a two pointer recursive function

        def quicksort(arr):
            # base case, return the input arr
            if len(arr) <= 1:
                return arr

            pivot = arr.pop()
            less_than = []
            greater_than = []
            # inductive step / sub problem
            for num in arr:
                if num <= pivot:
                    less_than.append(num)
                else:
                    greater_than.append(num)
            
            return quicksort(less_than) + [pivot] + quicksort(greater_than)

        nums = quicksort(nums)

        res = []
        for i, num in enumerate(nums):
            # Since the array is sorted, if num is positive
            # All proceeding values will also be positive and it will be impossible to solve for this case
            if num > 0:
                break

            # Check if the previous value is the same as current
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            # Since we are checking all unique permutations
            # We initialise i to the right of a
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # append the result
                    res.append([nums[i], nums[l], nums[r]])
                    # move both pointers in because we don't want to consider duplicates
                    l += 1
                    r -= 1
                    # if left is a duplicate, we need to move it again
                    # we can ignore updating the right pointer if duplicate
                    # because the above decrement will handle the right pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
        
