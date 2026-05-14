class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indexes:
                return [indexes[diff], i]
            indexes[n] = i