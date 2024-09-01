class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print('nums', nums)
        # can we solve this with one loop?
        def sum_vals(array):
            total = 1
            for i in range(len(array) - 1):
                total = total * array[i]
            return total

        result = []
        
        for i in range(len(nums)):
            new_nums = nums[:]
            new_nums[i], new_nums[-1] = new_nums[-1], new_nums[i] 
    
            result.append(sum_vals(new_nums))

        return result
