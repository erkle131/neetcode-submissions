class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = count = 0
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
            max_ones = max(max_ones, count)
        return max_ones