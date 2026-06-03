class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = 1

        L = 0
        prev = ""
        for R in range(1, len(arr)):
            if arr[R - 1] > arr[R] and prev != ">":
                length = max(length, R - L + 1)
                prev = ">"
            elif arr[R - 1] < arr[R] and prev != "<":
                length = max(length, R - L + 1)
                prev = "<"
            else: # arr[R - 1] == arr[R] or same compare twice (< <)
                L = R if arr[R - 1] == arr[R] else R - 1
                # Refresh prev based on the pair that triggered the else
                if arr[R - 1] > arr[R]: prev = ">"
                elif arr[R - 1] < arr[R]: prev = "<"
                else: prev = ""
        return length