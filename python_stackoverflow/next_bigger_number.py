
# https://stackoverflow.com/questions/61719835/increasing-itertools-permutations-performance

import itertools
def next_bigger2(n):
    num = str(n)
    num1 = set(int(x) for x in str(num))
    if num == num[0] *len(num):
        return -1
    #full_set = set(num)
    lis = set(int(''.join(nums)) for nums in itertools.permutations(num, len(num)))   
    lis = sorted(lis)
    try:
        return int(lis[lis.index(n)+1])
    except Exception:
        return -1

# this is a basic bubble sort algorithm (Which is kind of a simple but efficent sorting algorithm)
def sort_ascendant( arr:list  = [4,8,3,6,23,90,2] ):
    if len(arr)<=0 : raise ValueError("Array too small")

    keep_looping = True
    ret_arr = list(arr)

    while keep_looping:
        
        keep_looping = False # start false to exit by default

        for i, item in enumerate(ret_arr):
            
            if i >= len(ret_arr) - 1:
                # we r already on the last item so no need to sort
                break

            elif item <= ret_arr[i+1]:
                #do nothing
                pass

            elif item > ret_arr[i+1]:
                #reverse the order
                aux = ret_arr[i]
                ret_arr[i] = ret_arr[i+1]
                ret_arr[i+1] = aux

                keep_looping = True # if at least one item if sorted check again

    return ret_arr


def next_bigger(n):
    num_string = list(str(n))
    for i in range(1, len(num_string)):
        if i == len(num_string):
            return -1
    
        #find two the two numbers one bigger than the other with the minimun order
        if num_string[-i] > num_string[-i-1]:

            compare_reference = num_string[-i]
            index_reference = -i

            #check if the current number is smaller than any of the tail 
            for k, current in enumerate(num_string[-i:]):
                if num_string[-i-1] < current and current < compare_reference:
                    compare_reference = current
                    index_reference = -i+k
                    print("index num: " + str(index_reference))

            print("next bigger num: " + compare_reference)
            print("pivot: " + num_string[-i-1])


            #interchange the locations:
            num_string[index_reference] = num_string[-i-1]
            num_string[-i-1] = compare_reference



            #check if the tail is larger than one digit
            if i > 1:
                #order the rest of the vector to create the smaller number (ordering it).
                lower_part_ordered = sort_ascendant(num_string[-i:])
            else:
                lower_part_ordered = [num_string[-i]]
            
            # create a string from the list
            return int("".join(num_string[:-i] + lower_part_ordered))        

    # no match found means a number like 65311
    return -1

print(next_bigger(35421))
print(next_bigger(454321))
print(next_bigger(76422211))
print(next_bigger(12))
print(next_bigger(513342342342342342234))


