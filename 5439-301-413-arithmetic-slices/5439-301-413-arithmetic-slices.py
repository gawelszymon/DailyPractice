#jesli znajde podciag min 3 elementowy to przesuwam na prawo i ustawiam zmianna poprzdnipodciag na True, jesli kolejny element nie jest podciagiem to zmienna zmienia wartość na False, gdy jest podciag i zmienna jest na true to wtedy dodaje dwa do ilosci podciagów, a jesli jest false to tylko 1 
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        isA = False
        a = 0
        tc = 1
        if len(nums) > 1:
            for i in range(2, len(nums)):
                if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                    a += 1
                    if isA:
                        a += 1*tc
                        tc+=1
                    isA = True
                else:
                    isA = False
                    tc = 1
        return a

        