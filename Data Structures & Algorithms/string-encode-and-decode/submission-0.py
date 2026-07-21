class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append(str(len(s)) + '#' + s)
        return "".join(x for x in ans)

    def decode(self, s: str) -> List[str]:
        ans, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ans.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return ans