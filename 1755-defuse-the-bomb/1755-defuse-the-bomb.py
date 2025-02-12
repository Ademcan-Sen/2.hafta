class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        liste = []
        for _ in range(n):
            liste.append(0)
        if k==0: return liste
        elif k>0:
            liste[0]=sum(code[1:k+1])
            toplam=liste[0]
            for l in range(1, n):
                r=(l+k)%n
                toplam+=-code[l]+code[r]
                liste[l]= toplam
            return liste
        else:
            liste[0]=sum(code[-1:k-1:-1])
            toplam=sum(code[-1:k-1:-1])
            for l in range(1, n):
                r=(l-k)%n
                toplam+=-code[-l]+code[-r]
                liste[-l]= toplam
            return liste

        