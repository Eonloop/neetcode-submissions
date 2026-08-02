class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictCounter = defaultdict(int)
        for num in nums:
            dictCounter[num] += 1

        ranked = sorted(dictCounter.items(), key=lambda kv: kv[1], reverse=True)
        return [num for num, _ in ranked[:k]]