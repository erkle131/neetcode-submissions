class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}

        for i in nums:
            if i in num_count:
                num_count[i] += 1
                if num_count[i] == 2: return True
            else:
                num_count[i] = 1
        
        return False

