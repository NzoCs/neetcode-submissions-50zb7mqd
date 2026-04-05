class Solution:
    def isPalindrome(self, s: str) -> bool:

        def getAlphanumeric(s: str) -> str :

            s = s.lower()
            res = ""
            for i in range(len(s)):
                if s[i] != " " and s[i].isalnum():
                    res += s[i]
            
            return res

        s = getAlphanumeric(s)

        if len(s) <= 1 :
            return True

        if len(s) % 2 == 0 :
            Rptr = len(s)//2
            Lptr = len(s)//2 - 1
        else :
            Rptr = len(s)//2
            Lptr = len(s)//2

        while Lptr >= 0 :

            if s[Lptr] != s[Rptr] :
                return False

            Rptr += 1
            Lptr -= 1
        
        return True
        