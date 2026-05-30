class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Iterate through the array and push heights[i] on a stack.
        # If the next value is larger, we can continue to extend the
        # rectangle
        # If the next value is smaller, compute the area and see if
        # it's larger than our current max

        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area