class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_10 = int(a, 2)
        b_10 = int(b, 2)

        return bin(a_10 + b_10)[2:]
