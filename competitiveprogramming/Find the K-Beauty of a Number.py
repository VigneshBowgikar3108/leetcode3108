class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        A=str(num)
        c=0
        for i in range(k,len(A)+1):
            win=int(A[i-k:i])
            if  win!=0 and num % win==0:
                c+=1
        return c
            
            