class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        frequency = [[] for i in range(len(nums) + 1)]
        counter = Counter(nums)
        
        for num, count in counter.items():
            frequency[count].append(num)

        res = []
        for i in range(len(frequency)-1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res