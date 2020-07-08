class Solution:
    def reverseBits(self, n: int) -> int:
        
        # fill the binary representation with ceros:
        binary_string = bin(n)[2:]
        binary_string= "".join( (32 - len(binary_string)) * ["0"]) + binary_string
        int_value = 0

        # use inverse logic to calculate the int value
        for i, bit in enumerate(binary_string):
            if bit == "1":
                int_value += 2 ** i

        return int_value

sol = Solution()
print(sol.reverseBits(10))