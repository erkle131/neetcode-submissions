class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window_count = defaultdict(int)

        have, need = 0, len(countT)
        res, length = [-1, -1], float('inf')

        L = 0
        for R in range(len(s)):
            char = s[R]
            window_count[char] += 1

            if char in countT and window_count[char] == countT[char]:
                have += 1

            while have == need:
                if (R - L + 1) < length:
                    res = [L, R]
                    length = R - L + 1

                left_char = s[L]
                window_count[left_char] -= 1
                if left_char in countT and window_count[left_char] < countT[left_char]:
                    have -= 1
                L += 1

        L, R = res
        return s[L : R + 1] if length != float('inf') else ""