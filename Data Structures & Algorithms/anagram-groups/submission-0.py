class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            anagram = [0] * 26
            for ch in s:
                anagram[ord(ch) - ord('a')] += 1
            anagram = tuple(anagram)

            if anagram in groups:
                groups[anagram].append(s)
            else:
                groups[anagram] = [s]

        return [group for group in groups.values()]