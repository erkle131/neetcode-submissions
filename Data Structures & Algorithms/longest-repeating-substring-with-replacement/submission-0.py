class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        length = 0

        L = 0
        maxf = 0
        for R in range(len(s)):
            char_count[s[R]] = 1 + char_count.get(s[R], 0)
            maxf = max(maxf, char_count[s[R]])

            if (R - L + 1) - maxf > k:
                char_count[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length