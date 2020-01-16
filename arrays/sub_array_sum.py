
"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15

"""

def sub_array_sum(arr:list  = [4, 8, 3, 6, 1, 0, 23, 90, 2], wanted_sum:int = 10, sub_arr_len = 4 )-> int:
    #find a continuous sub-array which adds to a given number S
    n = len(arr)

    for i in range(n - sub_arr_len):
        current_sum = sum(arr[i: i + sub_arr_len])
        
        if current_sum == wanted_sum:
            return i

    return None



if __name__ == '__main__': 

    a = [1,2,3,6,2,4,7,9,6,4,7,9,3,4]
    wanted_sum = 11
    sub_length = 3
    i = sub_array_sum(a, wanted_sum, sub_length)
    print(a)
    print("the sub array that adds: "+str(wanted_sum)+" with length: "+str(sub_length)+" is on: "+str(i))
    print("the array is: "+str(a[i: i + sub_length]))

