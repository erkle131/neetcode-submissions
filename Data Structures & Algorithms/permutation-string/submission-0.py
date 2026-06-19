class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = {}
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)

        seen = {}
        L = 0
        for R in range(len(s2)):
            seen[s2[R]] = 1 + seen.get(s2[R], 0)

            if (R - L + 1) > len(s1):
                seen[s2[L]] -= 1
                if seen[s2[L]] == 0:
                    del seen[s2[L]] 
                L += 1

            if (R - L + 1) == len(s1):
                if seen == s1_count:
                    return True

        return False