class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}
        for c in s:
            char_count[c] = 1 + char_count.get(c, 0)

        for c in t:
            if c in char_count:
                char_count[c] -= 1

        if not any(char_count.values()):
            return True

        return False


