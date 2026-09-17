class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {}
        for i in s:
            freq_map[i] = freq_map.get(i, 0) + 1
        for j in t:
            freq_map[j] = freq_map.get(j, 0) - 1

        return all(v == 0 for v in freq_map.values())