class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for i, n in enumerate(nums):
            needed_num = target - n
            if needed_num in output:
                return [output[needed_num], i]
            output[n] = i