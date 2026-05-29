class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for each temp, push a pair (temp, index) onto the stack.
        # if the next element to be pushed onto the stack is greater,
        # compute the difference in indices between them and put the
        # result in the corresponding index in the output array

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append((temp, i))

        return res