class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_s = collections.defaultdict(list)
        for s in strs:
            ss = sorted(s)
            ss = ''.join(ss)
            if hash_s.get(ss,[]):
                hash_s[ss].append(s)
            else:hash_s[ss].append(s)
        result  = list()
        for v in hash_s.values():
            result.append(v)
        return result