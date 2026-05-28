class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # start window L and R at 0. Increment R up to k while summing values.
        # when we hit a window size of k, find the average
        # if the result is >= threshold, increment our result count
        L, res = 0, 0

        curSum = 0
        for R in range(len(arr)):
            curSum += arr[R]
            if R - L + 1 == k:
                avg = curSum / k
                if avg >= threshold:
                    res += 1
                curSum -= arr[L]
                L += 1

        return res