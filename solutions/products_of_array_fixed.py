class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate prefixes
        prefix_arr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            if i > 0:
                prefix_arr[i] *= prefix
            prefix *= nums[i]

        # calculate postfixes
        postfix_arr = [1] * len(nums)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                postfix_arr[i] *= postfix
            postfix *= nums[i]

        res = [1] * (len(nums))
        for i in range(len(nums)):
            res[i] = prefix_arr[i] * postfix_arr[i]

        return res
