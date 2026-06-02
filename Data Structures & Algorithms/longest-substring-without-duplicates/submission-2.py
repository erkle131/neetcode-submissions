class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        length = 0

        L = 0
        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])
            length = max(length, R - L + 1)
        return length