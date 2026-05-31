class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two pointer technique to calculate the amount
        # of water at each step and maintain a max so far
        # move the pointer with the smaller value because any
        # future container using index i will have a smaller width
        # and its height is still at most height[i]
        max_water = 0
        L, R = 0, len(heights) - 1

        while L < R:
            # calculate area using the shorter wall
            area = (R - L) * min(heights[L], heights[R])
            max_water = max(max_water, area)

            # move the pointer pointing to the shorter wall
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_water
