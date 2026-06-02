class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, cur_sum = 0, 0

        length = float("inf")
        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                length = min(length, R - L + 1)
                cur_sum -= nums[L]
                L += 1

        return 0 if length == float("inf") else length
