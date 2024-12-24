class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=""
        b=""
        c=""
        for i in s:
            if i.isalpha()==True:
                a=a+i
        a=a[::-1]
        a=list(a)
        s=list(s)
        for i in range(len(s)):
            if s[i].isalpha()==False:
                a.insert(i,s[i])
        for i in a:
            c=c+i
        return c
        