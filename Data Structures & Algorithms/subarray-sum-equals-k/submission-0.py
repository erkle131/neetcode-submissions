class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0 : 1}
        res = 0

        current_sum = 0
        for n in nums:
            current_sum += n
            diff = current_sum - k
            if diff in prefix_sums:
                res += prefix_sums[diff]
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)

        return res