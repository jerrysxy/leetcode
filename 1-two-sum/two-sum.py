class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for index, num in enumerate(nums):
            new_num = target - num
            if new_num in output:
                return [output[new_num], index]
            output[num] = index