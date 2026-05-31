class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] = 0 can be rearranged to:
        # -nums[i] = nums[j] + nums[k]
        # iterate through nums and find the j and k that satisfies
        # the above equation
        res = []

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break # Remaining numbers are all positive (no way to sum to zero)
            # skip the same element to avoid duplicate triples
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            L, R = i + 1, len(nums) - 1
            while L < R:
                if nums[L] + nums[R] > target:
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    # move pointers to the next unique elements
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1

        return res