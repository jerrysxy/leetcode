from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        counts = Counter(nums)

        for num, freq in counts.most_common(k):
            results.append(num)
            
        return results