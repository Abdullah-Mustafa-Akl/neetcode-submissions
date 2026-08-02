class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        searchNums = set(nums)
        longest = 0
        for n in nums:
            length = 1
            if n - 1 not in searchNums:
                t = n + 1
                while t in searchNums:
                    length += 1
                    t += 1
            longest = max(longest, length)
        return longest