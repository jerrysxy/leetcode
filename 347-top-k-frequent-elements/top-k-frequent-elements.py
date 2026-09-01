from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output =  []
        counts = Counter(nums)

        for number, count in counts.most_common(k):
            output.append(number)
        return output
