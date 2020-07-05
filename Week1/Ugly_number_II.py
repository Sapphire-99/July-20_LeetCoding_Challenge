class Solution:
    def nthUglyNumber(self, n: int) -> int:
        c2=c3=c5=0
        a=[1]
        while(n>1):
            next=min(2*a[c2],3*a[c3],5*a[c5])
            a.append(next)
            if next==2*a[c2]: 
                c2 += 1
            if next==3*a[c3]:
                c3 += 1
            if next==5*a[c5]:
                c5 += 1
            n =n-1
        return a[-1]
        
