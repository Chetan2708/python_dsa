class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        for i, char in enumerate(s):
            if char_count[ord(char) - ord('a')] == 1:
                return i
        return -1
