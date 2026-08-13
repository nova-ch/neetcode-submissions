from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length

        return result