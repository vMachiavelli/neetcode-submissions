class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = []
        maxl = 0

        for i in s:
            if i not in s1:
                s1.append(i)
            else:
                maxl = max(len(s1), maxl)
                idx = s1.index(i)
                s1 = s1[idx + 1:]
                s1.append(i)

        return max(maxl, len(s1))