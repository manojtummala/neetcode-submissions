class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s1 = []
        for s in strs:
            s1.append(str(len(s)))
            s1.append('#')
            s1.append(s)
        return ''.join(s1)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res