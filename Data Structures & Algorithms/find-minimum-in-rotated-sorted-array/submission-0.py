class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L < R:
            mid = L + (R - L) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        return nums[L]