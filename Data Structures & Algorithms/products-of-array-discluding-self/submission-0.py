class Solution:
    def productExceptSelf(self, nums: List[int]) -> None:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n

        total = 1
        for i in range(n):
            total *= nums[i]
            prefix[i] = total

        total = 1
        for i in range(n - 1, -1, -1):
            total *= nums[i]
            postfix[i] = total

        output = []
        for i in range(n):
            pre = prefix[i - 1] if i > 0 else 1
            post = postfix[i + 1] if i < len(nums) - 1 else 1
            output.append(pre * post)

        return output
            