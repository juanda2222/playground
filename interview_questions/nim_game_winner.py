class Solution:
    def canWinNim(self, n: int) -> bool:
        
        if n < 4:
            return True

        # case remove 1
        if (n - 1) % 4 is 0:
            return True

        # case # remove 2
        elif (n - 2) % 4 is 0:
            return True
            
        # case # remove 3
        elif (n - 3) % 4 is 0:
            return True

        # not exact means you will never win
        else:
            return False

sol = Solution()
print(sol.canWinNim(1))