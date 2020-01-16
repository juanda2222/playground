
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

def biggest_arrange(arr:list  = [4, 8, 3, 6, 1, 0, 23, 90, 2])-> int:
    #find a continuous sub-array which adds to a given number S

    if len(arr) <= 0 : raise ValueError("Array too small")
    if len(arr) <= 1 : return arr

    n = len(arr)

    ret_arr = list(range(n))
    single_digit_matrix = list(list())

    #create a multiple dimension array for the digits:
    for i  in range(n):
        string_digit_array = list(str(arr[i]))
        int_digit_arr = [int(string_digit) for string_digit in string_digit_array]

        # concatenate each array to the big array
        single_digit_matrix += [int_digit_arr]

    print(single_digit_matrix)


    # for the first line
    level = 0
    max_dgit_num = 3

    #order the single digit array using a counter algorithm (dictionary from 0 to 9)
    count_arr = [[0] * 10] * max_dgit_num

    for i in range(len(single_digit_matrix)):
        value = single_digit_matrix[i][level]
        #print("value is:"+str(value))
        count_arr[level][value] += -1
    
    print("the original count array is: "+str(count_arr))

    #modify the counting array acordng to a counting sort algorithm
    i = 1
    while i < len(count_arr[level]):
        count_arr[level][i] += count_arr[level][i - 1]
        i+=1
    

    count_arr[level] = list(map(lambda x: x + n, count_arr[level]))
    
    print("the MODIFIED count array is: "+str(count_arr))
    
    

    # create the return vector
    for i in range(len(arr)):

        value = single_digit_matrix[i][level]
        #print("dic index: "+str(dic_index))
        ret_index = count_arr[level][value] 
        #print("ret index: "+str(ret_index))
        count_arr[level][value] += -1
        #print("count_arr: "+str(ret_index))
        ret_arr[ret_index] = single_digit_matrix[i]


    return ret_arr



if __name__ == '__main__': 

    a = [1,2,23,26,32,34,7,449,46,44,7,901,31,94]
    big_n = biggest_arrange(a)
    print("the biggest possible number is: "+str(big_n))


