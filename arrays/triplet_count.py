
"""
Given an array of distinct integers. The task is to 
count all the triplets such that sum of two elements 
equals the third element.

Input:
The first line of input contains an integer T 
denoting the number of test cases. Then T test cases 
follow. Each test case consists of two lines. First 
line of each test case contains an Integer N denoting 
size of array and the second line contains N space 
separated elements.

Output:
For each test case, print the count of all triplets, 
in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5

"""

def triplet_count(arr:list  = [4, 8, 3, 6, 1, 0, 23, 90, 2])-> int:
    #find a continuous sub-array which adds to a given number S
    n = len(arr)
    count = 0

    for i in range(n - 2):
        if sum(arr[i: i + 2]) == arr[i + 2]:
            count += 1 

    return count

if __name__ == '__main__': 

    a = [1,2,3,6,2,4,7,9,6,4,7,9,3,4,7,11]
    i = triplet_count(a)
    print(a)
    print("the trplet count is: "+str(i))

