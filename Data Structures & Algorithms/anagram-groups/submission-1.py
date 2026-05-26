class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams become identical to one another when sorted
        # Loop through strs and sort each one and use as a key
        # in a HashMap, the value will be a list of the anagrams that match
        # the sorted key
        # result will be the values in the hashmap

        anagram_groups = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            anagram_groups[sortedS].append(s)

        return list(anagram_groups.values())