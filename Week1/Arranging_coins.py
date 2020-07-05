import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        d= 1+8*n
        
        sol= (-1+math.sqrt(d))//2
        return int(sol)
