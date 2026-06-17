class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        frequency = [[] for i in range(len(nums))]
        counter = Counter(nums)
        
        for num, count in counter.items():
            frequency[count-1].append(num)

        res = []
        for i in range(len(frequency)-1, -1, -1):
            if not k:
                break
            for num in frequency[i]:
                res.append(num)
                k -= 1

        return res