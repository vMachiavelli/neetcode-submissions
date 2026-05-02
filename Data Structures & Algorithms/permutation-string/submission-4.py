class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        for i in range(0, len(s2) - ls1 + 1):
            print(s2[i:i + ls1])
            if sorted(s1) == sorted(s2[i:i + ls1]):
                return True
        return False