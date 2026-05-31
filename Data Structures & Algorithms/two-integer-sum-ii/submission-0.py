class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numIndex = {} # key: num, val: index

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in numIndex:
                return [numIndex[diff] + 1, i + 1]
            numIndex[n] = i