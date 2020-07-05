class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor= x ^ y
        hamming_bit=0
        while(xor):   
            xor = xor & (xor -1)
            hamming_bit += 1
        return hamming_bit
            
        
