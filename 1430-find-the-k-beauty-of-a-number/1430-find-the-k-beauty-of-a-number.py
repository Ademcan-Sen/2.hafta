class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        sayac=0
        pairs = [str(num)[i:i+k] for i in range(len(str(num))-k+1)]
        for i in pairs:
            if int(i)==0:
                sayac=sayac
            elif num % int(i)==0:
                sayac+=1    
        return sayac
        