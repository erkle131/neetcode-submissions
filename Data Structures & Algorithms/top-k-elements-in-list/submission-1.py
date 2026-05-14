class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequency of each number
        count_map = {}
        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0)

        # 2. Use Bucket Sort: index is frequency, value is list of numbers
        # The max frequency possible is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count_map.items():
            buckets[freq].append(num)

        # 3. Iterate backwards from the highest frequency bucket
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
