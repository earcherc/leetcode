class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            b = target - num
            if b in dict:
                return [dict[b], i]
            
            dict[num] = i
