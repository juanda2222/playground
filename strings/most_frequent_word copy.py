
"""
Given an array containing N words consisting of lowercase 
characters. Your task is to find the most frequent word in 
the array. If multiple words have same frequency, then 
print the word whose first occurence occurs last in the 
array as compared to the other strings with same frequency.

Input:
The first line of the input contains a single integer T, 
denoting the number of test cases. Then T test case follows. 
Each test case contains 2 lines, the size of array N and 
N words separated by spaces.

Output:
For each testcase, output the most frequent word.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Example:
Input:
3
3
geeks for geeks
2
hello world
3
world wide fund

Output:
geeks
world
fund

Explanation:
Testcase 1: "geeks" comes 2 times.
Testcase 2: "hello" and "world" both have 1 frequency. 
We print world as it comes last in the input array.
"""

def most_frequent_word(string:str  = "sdf dd sdd sd ss dd sdf sdf")-> int:
    
    string_arr = string.split(" ") # get a list that we can traverse
    input_dic = dict() # use it as a counting device

    max_num = 0
    repeated_word = ""

    # create a dictionary to see wich is the most repeated word
    for word in string_arr:
        
        try:
            input_dic[word] += 1

            # grab the bigest one
            if input_dic[word] >= max_num:
                max_num = input_dic[word]
                repeated_word = word
            
        # initialize the counter in 1
        except KeyError:
            input_dic[word] = 1


    print(input_dic)

    return repeated_word



if __name__ == '__main__': 

    string = "as as as sd sd ew dw sd sd as sdf ew sdfdf frg"
    word = most_frequent_word(string)
    print("The most repeated word is: "+word)



