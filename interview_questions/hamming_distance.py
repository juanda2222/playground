class Solution:
    def hammingDistance(self, x: int, y: int) -> int:    

        #remove the "0b" from the strings:
        x_string = bin(x)[2:]
        y_string = bin(y)[2:]
        
        # see wich one is bigger and normalize size
        count = 0
        size_x = len(x_string)
        size_y = len(y_string)

        # x bigger:
        if size_x > size_y:
            big_size = size_x
            difference = size_x - size_y
            y_string = "".join(["0"] * difference) + y_string
        # y bigger:
        else:
            big_size = size_y
            difference = size_y - size_x
            x_string = "".join(["0"] * difference) + x_string

        #loop an count each diference
        for i in range(big_size):
            if x_string[i] is not y_string[i]:
                print("in")
                count+=1

        return count

sol = Solution()
print(sol.hammingDistance(1, 7))