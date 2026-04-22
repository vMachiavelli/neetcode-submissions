class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = (((s.strip("?!/(),.")).replace(" ",'')).lower()).strip("'")
        temp = temp.replace(",",'')
        temp = temp.replace("'",'')
        temp = temp.replace(":",'')
        print(temp)
        for i in range(len(temp)):
            if temp[i] != temp[-i - 1]:
                return False
        
        return True