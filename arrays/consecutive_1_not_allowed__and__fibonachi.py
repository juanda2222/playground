
"""
Given a positive integer N, count all possible distinct 
binary strings of length N such that there are no 
consecutive 1’s. Output your answer mod 10^9 + 7.

Input:
The first line of input contains an integer T denoting 
the number of test cases. The description of T test cases 
follows.
Each test case contain an integer N representing length 
of the binary string.

Output:
Print the count number of binary strings without 
consecutive 1’s of length N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
3
2

Output:
5
3

Explanation:
Testcase 1: case 5 strings are (000, 001, 010, 100, 101)
Testcse 2:  case 3 strings are (00,01,10)
"""

def fibonachi(n_position: int) -> int:
    if n_position == 0:
        return 0
    elif n_position == 1:
        return 1
    else:
        return fibonachi(n_position - 2 ) + fibonachi(n_position - 1)


def number_of_binarys(lenght:int  = 3)-> int:
    
    num_strings = fibonachi(lenght) + fibonachi(lenght + 1)

    return num_strings



if __name__ == '__main__': 

    lenght = 4
    num = number_of_binarys(lenght)
    print("with lenght: "+str(lenght)+" the number of strings is: "+str(num))



