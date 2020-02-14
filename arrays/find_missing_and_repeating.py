
"""
Given an unsorted array of size N of 
positive integers. One number 'A' from 
set {1, 2, …N} is missing and one number 
'B' occurs twice in array. Find these 
two numbers.

Note: If you find multiple answers then 
print the Smallest number found. Also, 
expected solution is O(n) time and 
constant extra space.

Input:
The first line of input contains an integer 
T denoting the number of test cases. The 
description of T test cases follows. The 
first line of each test case contains a 
single integer N denoting the size of array. 
The second line contains N space-separated 
integers A1, A2, ..., AN denoting the 
elements of the array.

Output:
Print B, the repeating number followed 
by A which is missing in a single line.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
1 ≤ A[i] ≤ N

Example:
Input:
2
2
2 2
3 
1 3 3

Output:
2 1
3 2

Explanation:
Testcase 1: Repeating number is 2 and smallest positive missing number is 1.
Testcase 2: Repeating number is 3 and smallest positive missing number is 2.
"""

def repeated_and_missing(arr:list  = [2,1,3,1])-> int:
    
    n = len(arr) #goes from 1 to n+1
    seeker_list = [1] * n

    for i, num in enumerate(arr):

        # repeated found
        if seeker_list[num - 1] == -1:
            repeated = num

        seeker_list[num - 1] = -1

    missing = seeker_list.index(1) + 1 # this might give a o(2n) complexity

    return (repeated, missing)



if __name__ == '__main__': 

    a = [1,2,3,14,13,12,4,5,12,11,7,8,9,10]
    (repeated, missing) = repeated_and_missing(a)
    print("the repeated is: "+str(repeated)+" and the missing is: "+str(missing))



