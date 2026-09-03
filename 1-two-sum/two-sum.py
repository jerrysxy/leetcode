class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for index, number in enumerate(nums):
            num_i_want = target - number
            if num_i_want in output:
                return [output[num_i_want],index]
            output[number] = index