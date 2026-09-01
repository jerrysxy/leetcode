class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i, n in enumerate(nums):
            other_n = target - n
            if other_n in output:
                return [output[other_n], i]
            output[n] = i
        