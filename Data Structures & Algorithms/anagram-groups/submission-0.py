class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            sstr = ''.join(sorted(string))
            if sstr not in seen:
                seen[sstr] = [string]
            else:
                seen[sstr].append(string)
        
        ret = []
        for i in seen:
            ret.append(seen[i])
            
        return ret