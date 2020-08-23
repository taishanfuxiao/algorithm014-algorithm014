class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        hash_s = Counter(s)
        for c in t:
            if hash_s.get(c,0) > 0:
                hash_s[c] = hash_s[c] - 1
            else:return False
        for v in hash_s.values():
            if v > 0:
                return False
        return True