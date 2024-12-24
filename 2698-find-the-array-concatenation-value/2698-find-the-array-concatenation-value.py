class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        liste=[]
        sayi1=len(nums)
        sayi=int(sayi1/2)
        sayac=0
        toplam=0
        ekleme=""
        while sayac<sayi:
            ekleme=ekleme+str(nums[0])+str(nums[-1])
            toplam=toplam+int(ekleme)
            del nums[0]
            del nums[-1]
            ekleme=""
            sayac+=1
        if sayi1 % 2!=0:
            toplam = toplam + nums[0]
        return toplam