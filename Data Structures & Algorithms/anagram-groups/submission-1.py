class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for st in strs:
            key = tuple(sorted(st))
            # print(tuple(sorted(st)))
            dictionary[key].append(st)

        return [res for res in dictionary.values()]